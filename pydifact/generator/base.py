from typing import List
from xml.dom import minidom
from xml.etree import ElementTree


class UntidBaseParser:
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

    def _validate_input(self, file_path: str) -> None:
        raise NotImplementedError

    def _process(self, file_path: str) -> None:
        raise NotImplementedError
