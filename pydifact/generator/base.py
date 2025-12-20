import re
from os import PathLike
from typing import List
from xml.dom import minidom
from xml.etree import ElementTree


class UntidBaseParser:
    name: str = ""
    msg_xml: ElementTree.Element

    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def get_errors(self) -> List[str]:
        """Return a list of errors encountered during parsing."""
        return self.errors

    def get_warnings(self) -> List[str]:
        """Return a list of warnings encountered during parsing."""
        return self.warnings

    def has_errors(self) -> bool:
        """Check if any errors were encountered."""
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        """Check if any warnings were encountered."""
        return len(self.warnings) > 0

    def get_xml(self) -> str:
        """Return a formatted XML string."""
        rough_string = ElementTree.tostring(self.msg_xml, encoding="utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8")

    def _validate_input(self, file_path: PathLike | str) -> None:
        raise NotImplementedError

    def _process(self, file_path: PathLike | str) -> None:
        raise NotImplementedError

    def parse_repr(self, repr: str) -> tuple[str, bool, str]:
        """Parse representation string and return type, is_range, and number."""
        match = re.match(r"^(a?n?)(\.\.)?(\d+)", repr)
        if not match:
            return "", False, ""
        else:
            _range = match.group(2)
            return (
                match.group(1).strip(),
                _range.strip() != ".." if _range else False,
                match.group(3).strip(),
            )

    def parse_repr_line(self, row: str) -> tuple[str, bool, str]:
        """Parse representation string and return type, is_range, and number."""
        match = re.match(r"^.?\s{0,4}Repr: (a?n?(?:\.\.)?\d+).*", row)
        if not match:
            return "", False, ""
        else:
            return self.parse_repr(match.group(1))

    @staticmethod
    def title2name(title: str) -> str:
        """Format title:remove spaces and special chars, capitalize words"""
        for char in [","]:
            title = title.replace(char, " ")
        title = title.replace("/", " Or ")
        title = "".join(word.capitalize() for word in title.lower().split())
        # title = (
        #     title[0].lower() + title[1:] if title else ""
        # )
        for char in ["'", "-"]:
            title = title.replace(char, "")
        return title
