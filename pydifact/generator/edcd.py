import re
from xml.etree import ElementTree
from pathlib import Path
from typing import List, Dict, Any

from pydifact.generator.base import UntidBaseParser


class EDCDParser(UntidBaseParser):
    """Parser for EDIFACT Composite Data Element Directory (EDCD) files."""

    def __init__(self, file_path: str):
        super().__init__()
        self.msg_xml = ElementTree.Element("composite_data_elements")

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDCDParser: {str(e)}")
            raise

    def _validate_input(self, file_path: str) -> None:
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

    def _process(self, file_path: str) -> None:
        """Process EDCD file and build XML structure."""
        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.read()

        # Replace special character
        file_lines = file_lines.replace("\xc4", "-")

        # Split by separator line (70 dashes)
        edcd_list = re.split(r"-{70}", file_lines)

        if len(edcd_list) < 2:
            self.warnings.append(
                f"File may not be properly formatted - found only {len(edcd_list)} sections"
            )

        # Remove the first empty section
        edcd_list = edcd_list[1:]

        for edcd_element in edcd_list:
            element_list = re.split(r"[\r\n]+", edcd_element)

            segment_code = ""
            segment_title = ""
            segment_function = ""
            data_elements: List[Dict[str, Any]] = []

            def_xml = ElementTree.SubElement(self.msg_xml, "composite_data_element")

            i = 0
            while i < len(element_list):
                row = element_list[i]
                if len(row) < 1:
                    i += 1
                    continue

                # Parse segment name and change indicator
                if segment_code == "":
                    match = re.match(
                        r"[\s]{4}.{1,3}[\s]{0,2}([A-Z0-9]{4})\s+([A-Z\s]+)", row
                    )
                    if not match:
                        self.warnings.append(f"Could not parse segment header: {row}")
                        break

                    segment_code = match.group(1)
                    segment_title = match.group(2)
                    i += 1
                    continue

                # Parse function/description
                if segment_function == "":
                    match = re.match(r"[\s]{7}Desc: (.*)", row)
                    if match:
                        segment_function = match.group(1)
                        i += 1
                        while i < len(element_list) and len(element_list[i]) > 1:
                            match2 = re.match(r"^[\s]{13}(.*)", element_list[i])
                            if match2:
                                segment_function += " " + match2.group(1)
                                i += 1
                            else:
                                break
                        continue

                # Parse element list
                match = re.match(
                    r"[\d]{3}.{4}([\w]{4})\s([\w\s\/]{10,43})(?:([\w]{1})([\d\s]{5}))?(?:\s{1}([\w\d\.]{2,8}))*",
                    element_list[i],
                )
                if match:
                    data_element = {
                        "elementId": match.group(1),
                        "elementName": match.group(2).strip(),
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
                        if i >= len(element_list) or len(element_list[i]) < 1:
                            continue

                        match2 = re.match(
                            r"[\s]{12}([\w\s]{43})([\w]{1})([\d\s]{5})(?:\s{1}([\w\d\.]{2,8}))*",
                            element_list[i],
                        )
                        if not match2:
                            i += 1
                            continue

                        data_element["elementName"] += " " + match2.group(1).strip()
                        data_element["elementCondition"] = match2.group(2)
                        data_element["elementRepetition"] = match2.group(3).strip()
                        if match2.group(4):
                            data_element["elementType"] = match2.group(4).strip()

                    data_elements.append(data_element)

                i += 1

            # Add attributes to XML element
            def_xml.set("id", segment_code)

            segment_title = self.title2name(segment_title)

            def_xml.set("name", segment_title)
            def_xml.set("desc", segment_function)

            # Add child elements
            for child in data_elements:
                ctype = (
                    "composite_data_element" if child["composite"] else "data_element"
                )
                cdef_xml = ElementTree.SubElement(def_xml, ctype)
                cdef_xml.set("id", child["elementId"])

                if child.get("elementCondition") == "M":
                    cdef_xml.set("required", "true")
