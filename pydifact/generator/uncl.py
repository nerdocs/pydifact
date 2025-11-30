import re
from os import PathLike
from xml.etree import ElementTree
from pathlib import Path
from typing import List

from pydifact.generator.base import UntidBaseParser
from pydifact.generator.constants import MAX_LINE_LENGTH


class UNCLParser(UntidBaseParser):
    """Parser for EDIFACT UN/CEFACT Code List (UNCL) files."""

    name = "UNCL"

    def __init__(self, file_path: PathLike | str, is_prehistoric: bool = False):
        super().__init__()
        self.msg_xml = ElementTree.Element("data_elements")
        self.is_prehistoric = is_prehistoric

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in UNCLParser: {str(e)}")
            raise

    def _validate_input(self, file_path: PathLike | str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"UNCL file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"UNCL file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"UNCL file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: PathLike | str) -> None:
        """Process UNCL file and build XML structure."""
        try:
            with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
                file_lines = f.read()

            # Replace special characters
            file_lines = file_lines.replace("\xc4", "-")

            # Split by separator line (70 dashes)
            uncl_list = re.split(r"-{70}", file_lines)
            if len(uncl_list) < 2:
                # Split per lookahead pattern, search for the typical header
                uncl_list = re.split(r"(?=^\d{4}\s+\S.+)", file_lines, flags=re.M)

            if len(uncl_list) < 2:
                self.warnings.append(
                    f"File may not be properly formatted - found only {len(uncl_list)} sections"
                )

            # Remove the first empty section
            uncl_list = uncl_list[1:]

            processed_elements = 0

            for section_index, uncl_element in enumerate(uncl_list, start=1):
                value_value_found = False

                try:
                    lines = re.split(r"[\r\n]+", uncl_element)

                    element_status = ""
                    element_code = ""
                    element_title = ""
                    element_use = ""
                    element_description = ""
                    element_type = ""
                    element_max_size = ""
                    element_values: List[dict[str, str]] = []

                    i = 0
                    while i < len(lines):
                        row = lines[i].rstrip()
                        if len(row) < 1:
                            i += 1
                            continue

                        # Parse element header
                        if element_code == "":
                            match = re.match(
                                r"^(.{5})([0-9]{4}\s{2})(.{56})\[([A-Z]?)\]", row
                            )
                            if not match:
                                if self.is_prehistoric:
                                    # 1001  Document name, coded
                                    match = re.match(r"^()([0-9]{4})\s{2}(.*)", row)
                                else:
                                    # *    1001  Document name code                  [C]

                                    match = re.match(
                                        r"^(.{5})([0-9]{4})\s{2,8}(.*)", row
                                    )

                                if not match:
                                    self.warnings.append(
                                        f"Section {section_index}: Could not parse element header: {row}"
                                    )
                                    break

                                element_status = match.group(1).strip()
                                element_code = match.group(2).strip()
                                element_title = match.group(3).strip()
                                i += 1

                                if i >= len(lines):
                                    self.warnings.append(
                                        f"Section {section_index}: Unexpected end of section while parsing element header continuation"
                                    )
                                    break

                                # check usage in newer releases
                                if not self.is_prehistoric:
                                    match2 = re.match(
                                        r"^[\s]{11}(.*)\[([A-Z]?)\]", lines[i]
                                    )
                                    if not match2:
                                        self.warnings.append(
                                            f"Section {section_index}: Could not parse element usage: {lines[i]}"
                                        )
                                        element_title += " " + lines[i].strip()
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
                            if self.is_prehistoric:
                                # if there was already a code value found,
                                # no description will follow any more.
                                if not value_value_found:
                                    # check for a "codes" pattern within an element code,
                                    # and if no match, it must be a description
                                    match = re.match(
                                        r"^\s{6,9}((?:(?!\s{2})[\s\S])*)$", row
                                    )
                                    if match:
                                        element_description = row.strip()
                                        i += 1
                                        while i < len(lines) and len(lines[i]) > 1:
                                            row = lines[i]
                                            element_description += " " + row.strip()
                                            i += 1

                            else:
                                match = re.match(r"[\s]{5}Desc: (.*)", row)
                                if match:
                                    element_description = match.group(1)
                                    i += 1
                                    while i < len(lines) and len(lines[i]) > 1:
                                        match2 = re.match(r"^[\s]{11}(.*)", lines[i])
                                        if match2:
                                            element_description += " " + match2.group(1)
                                            i += 1
                                        else:
                                            break
                                    continue

                        # Parse representation
                        if element_type == "":
                            if self.is_prehistoric:
                                pass  # TODO
                            else:
                                match = re.match(r"^\s{5}Repr: (a?n?)[.]*(\d+)", row)
                                if match:
                                    element_type = match.group(1).strip()
                                    element_max_size = match.group(2).strip()
                                else:
                                    self.warnings.append(
                                        f"Section {section_index}: Could not parse representation: {row}"
                                    )
                                i += 1
                                continue

                        # Parse code values and their descriptions
                        if self.is_prehistoric:
                            # match e.g.:
                            #      AAQ     Container number
                            #      30      Health Care Industry ID number
                            #      67      Promissory note signed by a third party and endorsed by
                            #              a bank
                            #      RT      UN/ECE/TRADE/WP.4/GE.1/EDIFACT Rapporteurs Teams
                            match = re.match(r"([\s]{4,6})(\S.+?)\s{2,8}(.*)", row)
                        else:
                            # match e.g.:
                            #     5     Product performance report
                            #     142   Ship security procedures not maintained during ship-to-ship
                            match = re.match(r"(.{5})(.{5})\s(.*)", row)
                        if match:
                            value_change = match.group(1).strip()
                            value_value = match.group(2).strip()
                            value_title = match.group(3).strip()
                            value_description = ""
                            value_value_found = True
                            i += 1

                            if value_value == "":
                                continue

                            # search for a code value description.
                            # There is no reliable rule to distinguish between a text
                            # describing the value at the next line or a longer value
                            # itself that follows into the next line. The only hint
                            # we have is that the line can max contain 14 + 55 chars.
                            # If the line + the first word of the next line is longer
                            # than 55 chars, it is most probably a continuation of the
                            # value with a line break.
                            # If the line is shorter than that, the next line is a
                            # description of the value. This is a bad hack, but the
                            # best we have, as the EDIFACT "standard" docs are really
                            # badly structured.
                            while i < len(lines) and len(lines[i]) > 1:
                                if self.is_prehistoric:
                                    match3 = re.match(r"^[\s]{14}(.*)$", lines[i])
                                    if match3:
                                        first_word = match3.group(1).strip().split()[0]
                                        if len(row) + len(first_word) > MAX_LINE_LENGTH:
                                            value_title += " " + match3.group(1).strip()
                                        else:
                                            if value_description:
                                                value_description += " "
                                            value_description += match3.group(1).strip()
                                        i += 1
                                    else:  # no additional line found, break
                                        break
                                else:

                                    match2 = re.match(r"^[\s]{14}(.*)", lines[i])
                                    if match2:
                                        if value_description:
                                            value_description += " "
                                        value_description += match2.group(1).strip()
                                        i += 1
                                    else:
                                        # if a "Note:" is found, proceed to next
                                        match3 = re.match(r"^[\s]{11}(.*)", lines[i])
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

                    # Validate parsed data
                    if not element_code:
                        self.warnings.append(
                            f"Section {section_index}: No element code found, skipping section"
                        )
                        continue

                    if not element_values:
                        self.warnings.append(
                            f"Section {section_index}: No code values found for element {element_code}"
                        )
                    def_xml = ElementTree.SubElement(self.msg_xml, "data_element")

                    def_xml.set("id", element_code)

                    for codes in element_values:
                        try:
                            cdef_xml = ElementTree.SubElement(def_xml, "code")
                            cdef_xml.set("id", self._safe_encode(codes["value"]))
                            cdef_xml.set("title", self._safe_encode(codes["title"]))
                            cdef_xml.set("desc", self._safe_encode(codes["descr"]))
                        except Exception as e:
                            self.errors.append(
                                f"Section {section_index}: Error adding code for element {element_code}: {str(e)}"
                            )

                    processed_elements += 1

                except Exception as e:
                    self.errors.append(
                        f"Section {section_index}: Error processing section: {str(e)}"
                    )

            if processed_elements == 0:
                raise ValueError("No valid data elements were processed from the file")

            self._log_summary(processed_elements)

        except Exception as e:
            self.errors.append(f"Process error: {str(e)}")
            raise

    def _safe_encode(self, text: str) -> str:
        """Safely encode text to UTF-8."""
        if not text:
            return ""

        # Try to encode from ISO-8859-1 to UTF-8
        try:
            if isinstance(text, bytes):
                return text.decode("iso-8859-1")
            return text
        except (UnicodeDecodeError, AttributeError):
            # Last resort: return as-is
            return text

    def _log_summary(self, processed_elements: int) -> None:
        """Log processing summary."""
        summary = f"Processed {processed_elements} data elements successfully"
        if self.warnings:
            summary += f", with {len(self.warnings)} warnings"
        if self.errors:
            summary += f", with {len(self.errors)} errors"

        print(summary)

        if self.warnings:
            print("Warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if self.errors:
            print("Errors:")
            for error in self.errors:
                print(f"  - {error}")
