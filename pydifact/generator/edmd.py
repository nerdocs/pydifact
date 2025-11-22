import re
from xml.etree import ElementTree
from pathlib import Path
from typing import List, Dict, Any, Optional

from pydifact.generator.base import UntidBaseParser


class EDMDParser(UntidBaseParser):
    """Parser for EDIFACT Message Directory (EDMD) files."""

    name = "EDMD"

    def __init__(self, file_path: str):
        super().__init__()
        self.msg_xml = ElementTree.Element("message")

        try:
            self._validate_input(file_path)
            self._process(file_path)
        except Exception as e:
            self.errors.append(f"Critical error in EDMDParser: {str(e)}")
            raise

    def _arr_recursion(
        self,
        dct: dict[Any, Any],
        level: int,
        counter: int,
        segment: dict[str, Any],
        current_index: list[Optional[str]],
    ) -> dict[Any, Any]:
        """Recursively add a segment into a nested dict at a given level.

        The structure rules are:
        - Group levels are keyed by their group identifiers (strings like "SG1").
        - Segments at the target level are stored under their numeric position (int).
        """
        # Descend through group levels until we reach the target level
        if counter < level:
            next_counter = counter + 1
            key = current_index[next_counter]

            # Ensure we have some key to descend into; this should normally be set
            if key is None:
                key = f"_level_{next_counter}"
                # Keep index list consistent to avoid drifting
                if len(current_index) > next_counter:
                    current_index[next_counter] = key

            # Initialize or validate the next nested container as a dict
            if key not in dct or not isinstance(dct.get(key), dict):
                dct[key] = {}

            dct[key] = self._arr_recursion(
                dct[key], level, next_counter, segment, current_index
            )
            return dct

        # We are at the target level: insert the segment under its position
        pos = segment.get("position")
        try:
            pos_int = int(pos) if pos is not None else None
        except (TypeError, ValueError):
            pos_int = None

        if pos_int is None:
            # Fallback: append after the largest integer key
            existing_int_keys = [k for k in dct.keys() if isinstance(k, int)]
            pos_int = (max(existing_int_keys) + 1) if existing_int_keys else 1

        dct[pos_int] = segment
        return dct

    def _validate_input(self, file_path: str) -> None:
        """Validate input file exists and is readable."""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"EDMD file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError(f"EDMD file is empty: {file_path}")

        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(
                f"EDMD file is too large: {file_path} "
                f"({file_size / 1024 / 1024:.2f} MB)"
            )

    def _process(self, file_path: str) -> None:
        """Process EDMD file and build XML structure."""
        path = Path(file_path)
        if path.is_dir():
            self.errors.append(f"{file_path} is a directory")
            return

        with open(file_path, "r", encoding="iso8859-1", errors="replace") as f:
            file_lines = f.readlines()

        skip = True
        current_level = 0
        current_index: list[Optional[str]] = [None]

        xml_tree: dict[Any, Any] = {}
        defaults: Dict[str, str] = {}
        groups: Dict[str, Dict[str, Any]] = {}

        def_xml = ElementTree.SubElement(self.msg_xml, "defaults")

        for line in file_lines:
            # Replace special characters
            line = line.replace("\xc4", "-")
            line = line.replace("\xb3", "|")
            line = line.replace("\xd9", "+").replace("\xc1", "+").replace("\xbf", "+")

            # Parse message metadata
            match = re.match(r"[\s]{43}Message Type : ([A-Z]{6})\r?\n?", line)
            if match:
                defaults["0065"] = match.group(1)
                cdef_xml = ElementTree.SubElement(def_xml, "data_element")
                cdef_xml.set("id", "0065")  # Message type
                cdef_xml.set("value", match.group(1))

            match = re.match(r"[\s]{43}Version      : ([A-Z]{1})\r?\n?", line)
            if match:
                defaults["0052"] = match.group(1)
                cdef_xml = ElementTree.SubElement(def_xml, "data_element")
                cdef_xml.set("id", "0052")  # Message version number
                cdef_xml.set("value", match.group(1))

            match = re.match(r"[\s]{43}Release      : ([A-Z0-9]{3})\r?\n?", line)
            if match:
                defaults["0054"] = match.group(1)
                cdef_xml = ElementTree.SubElement(def_xml, "data_element")
                cdef_xml.set("id", "0054")  # Message type release number
                cdef_xml.set("value", match.group(1))

            match = re.match(r"[\s]{43}Contr. Agency: ([A-Z]{2})\r?\n?", line)
            if match:
                defaults["0051"] = match.group(1)
                cdef_xml = ElementTree.SubElement(def_xml, "data_element")
                cdef_xml.set("id", "0051")  # Controlling agency
                cdef_xml.set("value", match.group(1))

            # Skip until we find the header line
            if skip:
                if re.search(r"Pos\s+Tag Name\s+S\s+R", line):
                    skip = False
                continue

            line = line.strip()
            if len(line) < 10:
                continue

            # Parse segment line
            match = re.match(
                r"(\d{4,5})[X\*\+\|\s]+([\w\s]{4})(.{41})(.{2})\s+(\d{1,5})(.*)", line
            )
            if not match:
                continue

            parts = [match.group(i).strip() for i in range(1, 7)]

            if not parts[0] or not re.match(r"\d+", parts[0]):
                continue

            # Handle segment groups
            if parts[1] == "" and "Segment group" in parts[2]:
                level = parts[5].replace("-", "")
                current_level += 1

                # Extend list if needed
                while len(current_index) <= current_level:
                    current_index.append(None)

                sg_match = re.search(r"(\d+)", parts[2])
                if sg_match:
                    sg_index = f"SG{sg_match.group(1)}"
                    if sg_index not in groups:
                        parts[1] = sg_index
                        groups[sg_index] = self._create_segment(parts, False)

                    current_index[current_level] = sg_index
                continue

            # Create the segment (includes position and other attributes)
            segment = self._create_segment(parts)

            # Add to dict structure
            self._arr_recursion(xml_tree, current_level, 0, segment, current_index)

            # Handle level changes
            if parts[1] != "" and "Segment group" not in parts[2] and "-" in parts[5]:

                level = parts[5].replace("-", "")
                levels_to_remove = level.count("+")
                current_level -= levels_to_remove

                # Clean up current_index - simply truncate or set to None
                for k in range(len(current_index) - 1, current_level, -1):
                    if k < len(current_index):
                        current_index[k] = None

        # Build the XML
        self._recurse(xml_tree, self.msg_xml, groups)

    def _recurse(
        self, dct: dict, xml: ElementTree.Element, groups: Dict[str, Dict[str, Any]]
    ) -> None:
        """Recursively build XML structure from a parsed dict."""
        for index, attrs in dct.items():
            if isinstance(index, int) and isinstance(attrs, dict):
                seg_xml = ElementTree.SubElement(xml, "segment")
                seg_xml.set("id", attrs["id"])
                seg_xml.set("maxrepeat", attrs["maxrepeat"])
                if attrs.get("required"):
                    seg_xml.set("required", "true")

            elif isinstance(index, str):
                # Be defensive in case group metadata is missing
                tmp_attrs = groups.get(index, {"id": index, "maxrepeat": "1"})
                group_xml = ElementTree.SubElement(xml, "group")
                group_xml.set("id", tmp_attrs["id"])
                group_xml.set("maxrepeat", tmp_attrs["maxrepeat"])
                if tmp_attrs.get("required"):
                    group_xml.set("required", "true")
                self._recurse(attrs, group_xml, groups)

    def _create_segment(
        self, parts: List[str], with_name: bool = True
    ) -> dict[str, Any]:
        """Create a segment dictionary from parsed parts."""
        # parts: [position, tag, name, required, maxrepeat, level]
        segment: dict[str, Any] = {
            "id": parts[1],
            "maxrepeat": parts[4].replace("-", ""),
            "position": int(parts[0]) if parts and parts[0].isdigit() else parts[0],
        }

        if with_name:
            segment["name"] = parts[2]

        if parts[3] == "M":
            segment["required"] = "true"

        return segment
