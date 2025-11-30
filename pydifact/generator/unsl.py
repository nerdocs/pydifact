import re
from os import PathLike
from xml.etree import ElementTree
from pathlib import Path
from typing import List, Dict

from pydifact.generator.base import UntidBaseParser


class UNSLParser(UntidBaseParser):
    """Parser for EDIFACT UN Service List (UNSL) files."""

    name = "UNSL"

    def __init__(self, file_path: PathLike | str):
        super().__init__()
        self.msg_xml = ElementTree.Element("data_elements")

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in UNSLParser: {str(e)}")
            raise

    def _validate_input(self, file_path: PathLike | str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"UNSL file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"UNSL file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"UNSL file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: PathLike | str) -> None:
        """Process UNSL file and build XML structure."""
        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.read()

        if not file_lines:
            raise ValueError(f"Failed to read file: {file_path}")

        # Replace special character
        file_lines = file_lines.replace("\xc4", "-")

        # Split by separator line (70 dashes)
        unsl_list = re.split(r"-{70}", file_lines)

        if len(unsl_list) < 2:
            self.warnings.append(
                f"File '{file_path}' may not be properly formatted - found only {len(unsl_list)} sections"
            )

        # Remove first empty section
        unsl_list = unsl_list[1:]

        for unsl_element in unsl_list:
            lines = re.split(r"[\r\n]+", unsl_element)

            element_status = ""
            element_code = ""
            element_title = ""
            element_description = ""
            element_type = ""
            element_max_size = ""
            element_note = ""
            element_values: List[Dict[str, str]] = []

            i = 0
            while i < len(lines):
                row = lines[i]
                if len(row) < 1:
                    i += 1
                    continue

                # Parse element header
                if element_code == "":
                    match = re.match(r"^(.{2})([0-9\s]{6})(.{0,62})", row)
                    if not match:
                        self.warnings.append(f"Could not parse element header: {row}")
                        break

                    element_status = match.group(1).strip()
                    element_code = match.group(2).strip()
                    element_title = match.group(3).strip()
                    i += 1
                    continue

                # Parse description
                if element_description == "":
                    match = re.match(r".+Desc: (.*)", row)
                    if match:
                        element_description = match.group(1)
                        i += 1
                        while i < len(lines) and len(lines[i]) > 1:
                            match2 = re.match(r"^ {8,14}(.*)", lines[i])
                            if match2:
                                element_description += " " + match2.group(1)
                                i += 1
                            else:
                                break
                        continue

                # Parse representation
                if element_type == "":
                    match = re.match(r"^ +Repr: (a?n?)[.]*(\d+)", row)
                    if not match:
                        self.warnings.append(
                            f"Could not parse 'Repr 'representation: {row}"
                        )
                    else:
                        element_type = match.group(1).strip()
                        element_max_size = match.group(2).strip()
                    i += 1
                    continue

                # Parse note
                if element_note == "":
                    match = re.match(r"[\s]{5}Note:", row)
                    if match:
                        element_note = ""
                        i += 1
                        while i < len(lines) and len(lines[i]) > 1:
                            match2 = re.match(r"^[\s]{11}(.*)", lines[i])
                            if match2:
                                if element_note:
                                    element_note += " "
                                element_note += match2.group(1)
                                i += 1
                            else:
                                break
                        continue

                # Parse code values
                match = re.match(r"(.{3})(.{6})\s(.*)", row)
                if match:
                    value_change = match.group(1).strip()
                    value_value = match.group(2).strip()
                    value_title = match.group(3).strip()
                    value_description = ""
                    i += 1

                    if value_value == "":
                        continue

                    while i < len(lines) and len(lines[i]) > 1:
                        match2 = re.match(r"^[\s]{13}(.*)", lines[i])
                        if match2:
                            if value_description:
                                value_description += " "
                            value_description += match2.group(1).strip()
                            i += 1
                        else:
                            match3 = re.match(r"^[\s]{10}(.*)", lines[i])
                            if match3:
                                if match3.group(1).strip() == "Note:":
                                    break
                                if value_title:
                                    value_title += " "
                                value_title += match3.group(1).strip()
                                i += 1
                            else:
                                break

                    element_values.append(
                        {
                            "value": value_value,
                            "title": value_title,
                            "descr": value_description,
                        }
                    )
                    continue

                i += 1

            if not element_code:
                continue

            if not element_values:
                self.warnings.append(f"No code values found for element {element_code}")

            def_xml = ElementTree.SubElement(self.msg_xml, "data_element")
            # Add attributes to XML element
            def_xml.set("id", element_code)

            element_title = self.title2name(element_title)

            def_xml.set("name", element_title)
            def_xml.set("desc", element_description)
            def_xml.set("type", element_type)
            def_xml.set("maxlength", element_max_size)

            # Add child code elements
            for codes in element_values:
                cdef_xml = ElementTree.SubElement(def_xml, "code")
                cdef_xml.set("id", self._safe_encode(codes["value"]))
                cdef_xml.set("title", self._safe_encode(codes["title"]))
                cdef_xml.set("desc", self._safe_encode(codes["descr"]))

    def _safe_encode(self, text: str) -> str:
        """Safely encode text to UTF-8."""
        if not text:
            return ""

        try:
            if isinstance(text, bytes):
                return text.decode("iso-8859-1")
            return text
        except (UnicodeDecodeError, AttributeError):
            return text
