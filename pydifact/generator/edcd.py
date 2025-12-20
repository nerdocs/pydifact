import re
from os import PathLike
from xml.etree import ElementTree
from pathlib import Path
from typing import List, Dict, Any

from pydifact.generator.base import UntidBaseParser


class EDCDParser(UntidBaseParser):
    """Parser for EDIFACT Composite Data Element Directory (EDCD) files."""

    name = "EDCD"

    def __init__(
        self,
        file_path: PathLike | str,
        data_elements: ElementTree.Element | None = None,
    ):
        """
        Initialize EDCDParser.

        Args:
            file_path (str): Path to EDCD file.
            data_elements (ElementTree.Element): ElementTree object representing data elements.
                This is used to compare agains the data elements and, if differences
                arise, show them.
        """
        super().__init__()
        self.msg_xml = ElementTree.Element("composite_data_elements")
        self.data_elements = data_elements

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDCDParser: {str(e)}")
            raise

    def _validate_input(self, file_path: PathLike | str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"EDCD file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"EDCD file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"EDCD file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: PathLike | str) -> None:
        """Process EDCD file and build XML structure."""
        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.read()

        # Replace special characters
        file_lines = file_lines.replace("\xc4", "-")

        # Split by S000/C000 lines
        edcd_list = re.split(r"(?= +[CS]\d{3} +[A-Z/ ]+ *)", file_lines)

        if len(edcd_list) < 2:
            edcd_list = re.split(r"[-─\xc4]{70,}", file_lines)
            if len(edcd_list) < 2:
                self.warnings.append(
                    f"File '{file_path}' may not be properly formatted - found only {len(edcd_list)} sections"
                )

        # Remove the first empty section
        edcd_list = edcd_list[1:]

        for edcd_element in edcd_list:
            parts = re.split(r"[\r\n]+", edcd_element)

            composite_code = ""
            composite_title = ""
            composite_function = ""
            data_elements: List[Dict[str, Any]] = []

            i = 0
            while i < len(parts):
                row = parts[i].rstrip()
                if len(row) < 1:
                    i += 1
                    continue
                if row.startswith("---"):
                    i += 1
                    continue

                # Parse segment name and change indicator
                if composite_code == "":
                    match = re.match(
                        r"[*+ |X]*([A-Z][0-9]{3}) +([A-Z /]+)", row.strip()
                    )
                    if not match:
                        self.warnings.append(f"Could not parse segment header: {row}")
                        break

                    composite_code = match.group(1)
                    composite_title = match.group(2).strip()
                    i += 1
                    continue

                # Parse function/description
                if composite_function == "":
                    match = re.match(r" +Desc: (.*)", row)
                    if match:
                        composite_function = match.group(1).strip()
                        i += 1
                        while i < len(parts) and len(parts[i]) > 1:
                            match2 = re.match(r"^ {12,17}(.+)", parts[i])
                            if match2:
                                composite_function += " " + match2.group(1).strip()
                                i += 1
                            else:
                                break
                        continue

                # Parse element list
                match = re.match(
                    r"[\d]{3}.{4}([\w]{4})\s([\w\s\/]{10,43})(?:([\w]{1})([\d\s]{5}))?(?:\s{1}([\w\d\.]{2,8}))*",
                    parts[i],
                )
                if match:
                    data_element = {
                        "elementId": match.group(1),
                        "elementTitle": match.group(2).strip(),
                    }

                    # Check if composite (starts with 'C')
                    data_element["composite"] = match.group(1)[0] == "C"

                    if match.group(3):
                        data_element["elementCondition"] = match.group(3)
                        data_element["elementRepetition"] = match.group(4).strip()
                        if match.group(5):
                            data_element["elementType"] = match.group(5).strip()
                    else:
                        # Check second row
                        i += 1
                        if i >= len(parts) or len(parts[i]) < 1:
                            continue

                        match2 = re.match(
                            r"[\s]{12}([\w\s]{43})([\w]{1})([\d\s]{5})(?:\s{1}([\w\d\.]{2,8}))*",
                            parts[i],
                        )
                        if not match2:
                            i += 1
                            continue

                        data_element["elementTitle"] += " " + match2.group(1).strip()
                        data_element["elementCondition"] = match2.group(2)
                        data_element["elementRepetition"] = match2.group(3).strip()
                        if match2.group(4):
                            data_element["elementType"] = match2.group(4).strip()

                    data_elements.append(data_element)

                i += 1

            if not composite_code:
                continue

            def_xml = ElementTree.SubElement(self.msg_xml, "composite_data_element")

            # Add attributes to XML element
            def_xml.set("id", composite_code)

            composite_title = self.title2name(composite_title)

            def_xml.set("name", composite_title)
            def_xml.set("desc", composite_function)

            # Add child elements
            for child in data_elements:
                ctype = (
                    "composite_data_element" if child["composite"] else "data_element"
                )
                cdef_xml = ElementTree.SubElement(def_xml, ctype)
                cdef_xml.set("id", child["elementId"])

                # Preserve requirement flag
                if child.get("elementCondition") == "M":
                    cdef_xml.set("required", "true")

                # Enrich with additional details when available.
                title = child.get("elementTitle")
                if title:
                    cdef_xml.set("name", self.title2name(title))

                usage = child.get("elementCondition")
                if usage:
                    cdef_xml.set("usage", usage)

                repetition = child.get("elementRepetition")
                if repetition:
                    cdef_xml.set("repetition", repetition)

                el_type = child.get("elementType")
                if el_type:
                    element_type, is_fixed_length, length = self.parse_repr(el_type)
                    cdef_xml.set("type", element_type)
                    if is_fixed_length:
                        cdef_xml.set("length", length)
                    else:
                        cdef_xml.set("maxlength", length)
