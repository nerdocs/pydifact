import re
from os import PathLike
from xml.etree import ElementTree
from pathlib import Path

from pydifact.generator.base import UntidBaseParser


class EDEDParser(UntidBaseParser):
    """Parser for EDIFACT Data Element Directory (EDED) files.

    Args:
        file_path (str): Path to the EDED file.
        codes (ElementTree.Element): ElementTree containing codes, which will be
            included in the elements.
        is_prehistoric (bool, optional): Whether the EDED file is prehistoric (<99).
            Defaults to False.
        service (bool, optional): Whether service elements should be parsed.
            Defaults to False, which means it should parse data elements.
    """

    name = "EDED"

    def __init__(
        self,
        file_path: PathLike | str,
        codes: ElementTree.Element | None = None,
        is_prehistoric: bool = False,
        service: bool = False,
    ):
        super().__init__()
        self.is_prehistoric = is_prehistoric
        self.msg_xml = ElementTree.Element("data_elements")
        self.codes = codes
        self.service = service

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDEDParser: {str(e)}")
            raise

    def _validate_input(self, file_path: PathLike | str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"EDED file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"EDED file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"EDED file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: PathLike | str) -> None:
        """Process EDED file and build XML structure."""
        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.read()

        # Replace special characters
        file_lines = file_lines.replace("\xc4", "-")

        # Split by separator line (70 dashes)
        eded_list = re.split(r"(?=^\s{0,5}\d{4}\s+\S.+)", file_lines, flags=re.M)

        if len(eded_list) < 2:
            self.warnings.append(
                f"File '{file_path}' may not be properly formatted - found only {len(eded_list)} sections"
            )

        # Remove the first empty section
        eded_list = eded_list[1:]

        for eded_element in eded_list:
            parts = re.split(r"[\r\n]+", eded_element)

            element_status = ""
            element_code = ""
            element_title = ""
            element_use = ""
            element_description = ""
            element_type = ""
            element_length = ""
            is_range: bool = False
            element_note = ""

            i = 0
            while i < len(parts):
                row = parts[i].rstrip()
                if len(row) < 1:
                    i += 1
                    continue

                # Parse element header
                if element_code == "":
                    if self.is_prehistoric:
                        match = re.match(r"^()([\d]{4}\s)(.+?)\s{4,}(.*)", row)
                    else:
                        match = re.match(
                            r"^(.{5})([\d]{4}\s{2})(.{56})\[([A-Z]?)\]", row
                        )
                    if not match:
                        match = re.match(r"^ {2,5}([\d]{4})\s{2}(.*)", row)
                        if match:
                            element_code = match.group(1).strip()
                            element_title = match.group(2).strip()
                            i += 1
                            continue

                        match = re.match(r"^(.{5})([\d]{4}\s{2})(.*)", row)
                        if not match:
                            self.warnings.append(
                                f"Could not parse element header: {row}"
                            )
                            break

                        element_status = match.group(1).strip()
                        element_code = match.group(2).strip()
                        element_title = match.group(3).strip()
                        i += 1

                        if i >= len(parts):
                            self.warnings.append(
                                "Unexpected end of section while parsing element header continuation"
                            )
                            break

                        match2 = re.match(r"^[\s]{11}(.*)\[([A-Z]?)]", parts[i])
                        if not match2:
                            self.warnings.append(
                                f"Could not parse element usage: {parts[i]}"
                            )
                            element_title += " " + parts[i].strip()
                        else:
                            element_title += " " + match2.group(1).strip()
                            element_use = match2.group(2)
                        i += 1
                        continue

                    element_status = match.group(1).strip()
                    element_code = match.group(2).strip()
                    if self.service:
                        if int(element_code) >= 1000:
                            # if we should only parse service data elements, skip to next element
                            break
                    else:
                        if int(element_code) < 1000:
                            # if we should only parse data elements, skip to next element
                            break

                    element_title = match.group(3).strip()
                    element_use = match.group(4)
                    i += 1
                    continue

                # Parse description
                if element_description == "":
                    match = re.match(r"(?:.{1}\s{4})?Desc:\s(.*)", row)
                    if match:
                        element_description = match.group(1).strip()
                        i += 1
                        while i < len(parts) and len(parts[i]) > 1:
                            match2 = re.match(r"^\s{6,11}(.*)", parts[i])
                            if match2:
                                element_description += " " + match2.group(1).strip()
                                i += 1
                            else:
                                break
                        continue

                # Parse representation
                if element_type == "":
                    if "Repr: " in row:
                        element_type, is_range, element_length = self.parse_repr_line(
                            row
                        )
                    elif "Desc: " in row:
                        # Skip if it's a description and we haven't found a representation yet
                        # Some files have Desc and Repr swapped or missing Repr
                        pass
                    else:
                        element_type, is_range, element_length = self.parse_repr_line(
                            row
                        )

                    if not element_type and "Desc: " not in row:
                        self.warnings.append(
                            f"Could not parse representation in {element_code} "
                            f"element, line {i}: '{row}'"
                        )
                    if element_type:
                        i += 1
                        continue

                # Parse note
                if element_note == "":
                    match = re.match(r"^\s{0,5}Note: (.*)", row)
                    if match:
                        element_note = match.group(1).strip()
                    i += 1
                    while i < len(parts) and len(parts[i]) > 1:
                        match = re.match(r"^[\s]{6,11}(.*)", parts[i])
                        if match:
                            if element_note:
                                element_note += " "
                            element_note += match.group(1).strip()
                            i += 1
                        else:
                            break
                    continue

                i += 1

            if not element_code:
                continue

            def_xml = ElementTree.SubElement(self.msg_xml, "data_element")
            # Add attributes to XML element
            def_xml.set("id", element_code)

            element_title = self.title2name(element_title)

            def_xml.set("name", element_title)
            def_xml.set("usage", element_use)
            def_xml.set("desc", element_description)
            def_xml.set("type", element_type)
            if is_range:
                def_xml.set("length", element_length)
            else:
                def_xml.set("maxlength", element_length)

            # if codes are available, fill the codes into the tree
            if self.codes:
                codes_element = self.codes.find(f"./data_element[@id='{element_code}']")
                if codes_element:
                    for child in codes_element:
                        def_xml.append(child)
