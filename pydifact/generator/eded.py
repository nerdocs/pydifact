import re
from xml.etree import ElementTree
from pathlib import Path

from pydifact.generator.base import UntidBaseParser


class EDEDParser(UntidBaseParser):
    """Parser for EDIFACT Data Element Directory (EDED) files."""

    def __init__(self, file_path: str):
        super().__init__()
        self.msg_xml = ElementTree.Element("data_elements")

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDEDParser: {str(e)}")
            raise

    def _validate_input(self, file_path: str) -> None:
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

    def _process(self, file_path: str) -> None:
        """Process EDED file and build XML structure."""
        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.read()

        # Replace special characters
        file_lines = file_lines.replace("\xc4", "-")

        # Split by separator line (70 dashes)
        eded_list = re.split(r"-{70}", file_lines)

        if len(eded_list) < 2:
            self.warnings.append(
                f"File may not be properly formatted - found only {len(eded_list)} sections"
            )

        # Remove first empty section
        eded_list = eded_list[1:]

        for eded_element in eded_list:
            parts = re.split(r"[\r\n]+", eded_element)

            element_status = ""
            element_code = ""
            element_title = ""
            element_use = ""
            element_description = ""
            element_type = ""
            element_max_size = ""
            element_note = ""

            def_xml = ElementTree.SubElement(self.msg_xml, "data_element")

            i = 0
            while i < len(parts):
                row = parts[i]
                if len(row) < 1:
                    i += 1
                    continue

                # Parse element header
                if element_code == "":
                    match = re.match(r"^(.{5})([0-9\s]{6})(.{56})\[([A-Z]?)\]", row)
                    if not match:
                        match = re.match(r"^(.{5})([0-9\s]{6})(.*)", row)
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

                        match2 = re.match(r"^[\s]{11}(.*)\[([A-Z]?)\]", parts[i])
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
                    element_title = match.group(3).strip()
                    element_use = match.group(4)
                    i += 1
                    continue

                # Parse description
                if element_description == "":
                    match = re.match(r".{1}\s{4}Desc: (.*)", row)
                    if match:
                        element_description = match.group(1)
                        i += 1
                        while i < len(parts) and len(parts[i]) > 1:
                            match2 = re.match(r"^[\s]{11}(.*)", parts[i])
                            if match2:
                                element_description += " " + match2.group(1)
                                i += 1
                            else:
                                break
                        continue

                # Parse representation
                if element_type == "":
                    match = re.match(r"^.{1}\s{4}Repr: (a?n?)[\.]*(\d+)", row)
                    if not match:
                        self.warnings.append(f"Could not parse representation: {row}")
                    else:
                        element_type = match.group(1).strip()
                        element_max_size = match.group(2).strip()
                    i += 1
                    continue

                # Parse note
                if element_note == "" and re.match(r"[\s]{5}Note:", row):
                    element_note = ""
                    i += 1
                    while i < len(parts) and len(parts[i]) > 1:
                        match = re.match(r"^[\s]{11}(.*)", parts[i])
                        if match:
                            if element_note:
                                element_note += " "
                            element_note += match.group(1)
                            i += 1
                        else:
                            break
                    continue

                i += 1

            # Add attributes to XML element
            def_xml.set("id", element_code)

            # Format title: lowercase first, remove spaces, capitalize words
            element_title = element_title.lower()
            element_title = "".join(word.capitalize() for word in element_title.split())
            # element_title = (
            #     element_title[0].lower() + element_title[1:] if element_title else ""
            # )
            element_title = element_title.replace("/", "Or")

            def_xml.set("name", element_title)
            def_xml.set("usage", element_use)
            def_xml.set("desc", element_description)
            def_xml.set("type", element_type)
            def_xml.set("maxlength", element_max_size)
