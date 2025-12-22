import re
from os import PathLike
from xml.etree import ElementTree
from pathlib import Path
from typing import List, Dict, Any

from mypy.fastparse import Match

from pydifact.generator.base import UntidBaseParser


class EDSDParser(UntidBaseParser):
    """Parser for EDIFACT Segment Directory (EDSD) files."""

    name = "EDSD"

    def __init__(self, file_path: PathLike | str, is_prehistoric: bool = False):
        super().__init__()
        self.is_prehistoric = is_prehistoric
        self.msg_xml = ElementTree.Element("segments")

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDSDParser: {str(e)}")
            raise

    def _validate_input(self, file_path: PathLike | str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"EDSD file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"EDSD file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"EDSD file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: PathLike | str) -> None:
        """Process EDSD file and build XML structure."""
        with open(file_path, "r", errors="replace") as f:
            file_lines = f.read()

        # Replace special characters
        file_lines = file_lines.replace("\xc4", "-")  # replace "─" with "-"

        # Split by Segment headers
        if self.is_prehistoric:
            # snip preceeding blabla
            file_lines = re.split(
                r"SEGMENTS SPECIFICATIONS",
                file_lines,
                flags=re.MULTILINE | re.IGNORECASE,
            )[1]
            # split files at Segment headers, preserving them
            edsd_list = re.split(
                r"(?=^[ +*#|X]+[A-Z]{3} {1,3}[\w -,/]+(?: {4,}[()\d.][()\d. "
                r"]{2,11})?$)",
                file_lines,
                flags=re.M,
            )
        else:
            # split files at Segment headers, preserving them
            edsd_list = re.split(r"(?=^ {2,7}[A-Z]{3}  +\S*)", file_lines, flags=re.M)

        if len(edsd_list) < 2:
            self.warnings.append(
                f"File '{file_path}' may not be properly formatted - found only {len(edsd_list)} sections"
            )

        # Remove the first empty section
        edsd_list = edsd_list[1:]

        for edsd_item in edsd_list:
            parts = re.split(r"[\r\n]+", edsd_item)

            segment_code = ""
            segment_title = ""
            segment_function = ""
            data_elements: List[Dict[str, Any]] = []

            i = 0
            while i < len(parts):
                row = parts[i].rstrip()
                if len(row) < 1:
                    i += 1
                    continue

                # Parse segment name
                if segment_code == "":
                    if self.is_prehistoric:
                        match = re.match(
                            r"^[+*| ]*([A-Z]{3}) +([\w -,/]+?)(?: {4,}.*)?$",
                            row,
                        )
                    else:
                        match = re.match(r"[ +*#|X]+([A-Z]{3}) +(.+)", row)
                    if not match:
                        self.warnings.append(f"Could not parse segment header: '{row}'")
                        break

                    segment_code = match.group(1)
                    segment_title = match.group(2).strip()
                    i += 1
                    continue

                # Parse function
                if segment_function == "":
                    match = re.match(r"[\s|]?\s{,7}Function: (.*)", row)
                    if match:
                        segment_function = match.group(1)
                        i += 1
                        while i < len(parts) and len(parts[i]) > 1:
                            match_second_line = re.match(r"^[\s]{10,17}(.*)", parts[i])
                            if match_second_line:
                                segment_function += (
                                    " " + match_second_line.group(1).strip()
                                )
                                i += 1
                            else:
                                break
                        continue

                ## Parse element list, prehistoric:
                #     C198  PRODUCT IDENTIFICATION                      C
                #     C198    PRODUCT IDENTIFICATION                  C
                #  8053    EQUIPMENT QUALIFIER                     M  an..3  id 1  3
                #  C271    EQUIPMENT                               C
                #  8114      Transport equipment identification    C  an..4  an 1  4
                #            prefix number
                ##  ...and newer:
                # 010   C543 AGREEMENT TYPE IDENTIFICATION              C    1
                #       7433  Agreement type description code           C      an..3
                #       1131  Code list identification code             C      an..17

                # first check if it matches generally a data/composite element:
                match_generic = re.match(
                    r"[*+|X ]{0,5}(\d{3}|) *([CS\d]\d{3}) .+", parts[i]
                )
                if match_generic:
                    # we can be sure this is a composite/data element row.
                    element_pos = match_generic.group(1)
                    element_id = match_generic.group(2)
                    data_element = {
                        "elementId": element_id,
                    }
                    if not self.is_prehistoric:
                        # if in newer versions the descriptions are multiline,
                        # just concat them
                        if (
                            element_id[0] != "C"
                            and i + 1 < len(parts)
                            and len(parts[i + 1]) > 0
                        ):
                            match_second_line = re.match(
                                r"^ {11,14}(.+)$",
                                parts[i + 1],
                            )
                            if match_second_line:
                                i += 1
                                row = row + " " + parts[i].lstrip()

                    # First, try to match the top level data 1-line rows
                    if match := re.match(
                        r"^(\d{3}|)[*+|X ]*[CS\d]\d{3} +([A-Z,\- '\/]{7,}) +([MC])"
                        r"( *\d{1,3}|) *([an]+\.*\d{1,3}|) *(.+|)$",
                        row,
                    ):
                        # Extract composite data element attributes from matched row
                        element_pos = match.group(1)
                        element_repitition = (
                            "1" if self.is_prehistoric else match.group(4).strip()
                        )
                        data_element["elementRepetition"] = element_repitition
                        data_element["elementName"] = match.group(2).strip()
                        data_element["elementCondition"] = match.group(3)
                        data_element["elementDescription"] = match.group(6).strip()

                        if element_id[0] in ["C", "S"]:
                            data_element["composite"] = True
                        else:
                            data_element["composite"] = False
                            data_element["elementType"] = match.group(5)

                        # Data elements can have a second row containing a
                        # longer element name.
                        # in ancient versions, this is just built with a string
                        # that follows in the next line:
                        #    5427    Allowance/charge percent basis          C  an..3  id 1  3
                        #            qualifier
                        i += 1
                        if i < len(parts) and parts[i].strip():
                            match_second_line = re.match(
                                r"^ {11,14}(.+)$",
                                parts[i],
                            )
                            if match_second_line:
                                data_element["elementName"] += (
                                    " " + match_second_line.group(1).strip()
                                )

                        # if name consists only of CAPITALS, this is a top level
                        # element.
                        if re.match(r"^[A-Z,\- '\/]+$", data_element["elementName"]):
                            if data_element["composite"]:
                                data_element["children"] = []
                            data_elements.append(data_element)
                        else:
                            last_element = data_elements[-1]
                            # TODO: add children
                            last_element["children"].append(data_element)
                        continue

                    # Then find the sub elements
                    elif match := re.match(
                        r"^(\d{3}|)[*+|X ]*[CS\d]\d{3} +(.+) *([MC]) *"
                        r"(?:(\d{,3})?([an]+\.*\d{1,3})?(.*)?)?",
                        row,
                    ):
                        i += 1
                        continue
                        element_pos = match.group(1)
                        element_repitition = (
                            "1" if self.is_prehistoric else match.group(4)
                        )
                        data_element["elementName"] = match.group(2).strip()
                        data_element["elementCondition"] = match.group(3)
                        data_element["elementDescription"] = match.group(6).strip()

                        data_element["composite"] = False
                        data_element["elementType"] = match.group(5)

                        data_elements.append(data_element)
                    else:
                        self.warnings.append(
                            f'Could not parse possible element header: "{row}"'
                        )

                else:
                    # debug
                    # print("ignoring line:", row)
                    pass
                i += 1

            if not segment_code:
                continue
            if segment_code == "UNA":
                # UNA is so special, and not consistently documented in EDSD files, we
                # don't want to save that in XML, but generate it manually
                continue
            else:
                if not data_elements:
                    self.warnings.append(f"Segment {segment_code}: No elements found.")

            if (
                segment_code == "UNB"
                and self.msg_xml.find("segment[@id='UNA']") is None
            ):
                # ---- special case UNA header: create it manually just before UNB: ----
                def_xml = ElementTree.SubElement(self.msg_xml, "segment")
                def_xml.set("id", "UNA")
                def_xml.set("name", "ServiceStringAdvice")
                def_xml.set(
                    "desc",
                    "To define the characters selected for use as delimiters "
                    "and indicators in the rest of the interchange that follows",
                )

                cdef_xml = ElementTree.SubElement(def_xml, "data_element")
                # cdef_xml.set("id", "0000")
                # cdef_xml.set("title", "Service String Advice")
                cdef_xml.set("required", "true")
                cdef_xml.set("type", "an")
                cdef_xml.set("length", "6")
                # ----------------------------------------------------------------------

            def_xml = ElementTree.SubElement(self.msg_xml, "segment")
            # Add attributes to XML element
            def_xml.set("id", segment_code)

            segment_title = self.title2name(segment_title)

            def_xml.set("name", segment_title)
            def_xml.set("desc", segment_function)

            # Add child elements
            for top_level_element in data_elements:
                # check if the element was created successfully
                if "composite" not in top_level_element:
                    print(
                        f"❌ Element {top_level_element} in '{file_path}' is malformed "
                        f"(parsing error?), skipping..."
                    )
                    continue

                ctype = (
                    "composite_data_element"
                    if top_level_element["composite"]
                    else "data_element"
                )

                cdef_xml = ElementTree.SubElement(def_xml, ctype)
                cdef_xml.set("id", top_level_element["elementId"])
                cdef_xml.set("name", self.title2name(top_level_element["elementName"]))

                if top_level_element.get("elementCondition") == "M":
                    cdef_xml.set("required", "true")
                if top_level_element.get("elementDescription"):
                    cdef_xml.set("desc", top_level_element["elementDescription"])
                if top_level_element.get("elementRepetition"):
                    cdef_xml.set("repeat", top_level_element["elementRepetition"])
                if top_level_element.get("elementType"):
                    element_type, is_fixed_length, length = self.parse_repr(
                        top_level_element["elementType"]
                    )
                    cdef_xml.set("type", element_type)
                    if is_fixed_length:
                        cdef_xml.set("length", length)
                    else:
                        cdef_xml.set("maxlength", length)
