# These classes represent the elements, composite elements, segments and messages for
# the edifact parser that creates an internal representation of these data.
# Note that they are NOT used for pydifact itself, as the code that is used by
# pydifact is created on the fly by the parser and is located in
# syntax.xxx.{data|composite|messages}.py
import typing
from dataclasses import dataclass
from typing import NamedTuple

from .helpers import to_class_name, to_identifier


@dataclass
class DataElementSpec:
    """Specification of a data element, as described in the UNECE docs.

    This is used for a global list of data elements, as "master data".
    """

    code: str
    title: str
    repr_line: str
    description: str
    url: str = ""
    stub: bool = False

    def class_name(self) -> str:
        """Returns a Python class name that can be used as a dataclass."""
        prefix = "E" if int(self.code) >= 1000 else ""
        return to_class_name(self.title, prefix)

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as accessor in a dataclass."""
        return f"{to_identifier(self.title)}"


class CompositeDataElementUsage(NamedTuple):
    """Usage of a data element within a composite data element.

    The usage can differ in its representation ("an..10") and whether it is
    mandatory, from the original composite element.
    """

    pos: str
    element: DataElementSpec
    mandatory: bool
    repr_line: str = ""


# DataElement, mandatory, [repr]
@dataclass
class CompositeElementSpec:
    """Specification of a generic composite data element, as described in the UNECE
    docs."""

    code: str
    title: str
    schema: list[CompositeDataElementUsage]
    description: str = ""
    url: str = ""
    stub: bool = False

    def class_name(self) -> str:
        # CS = Composite Service
        # CU = Composite User
        prefix = "CS" if self.code.startswith("S") else "CU"
        return to_class_name(self.title, prefix)  # type: ignore

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as accessor in a dataclass."""
        return f"{to_identifier(self.title)}"


class SegmentDataElementUsage(NamedTuple):
    """Usage of a top level data element within a segment.

    The usage can differ in its representation ("an..10"), its "repeated" property and
    whether it is mandatory, from the original data element.
    """

    pos: str
    element: DataElementSpec
    mandatory: bool
    repeat: int
    repr_line: str = ""

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as accessor in a dataclass."""
        return f"{to_identifier(self.element.title)}"


class SegmentInlineDataElementUsage(NamedTuple):
    """Usage of a top level data element within a segment."""

    element: DataElementSpec
    mandatory: bool
    repr_line: str = ""


class SegmentCompositeElementUsage(NamedTuple):
    """Usage of a top level composite data element within a segment."""

    pos: str
    element: CompositeElementSpec
    mandatory: bool
    repeat: int = 1
    schema: list[SegmentInlineDataElementUsage] | None = None

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as accessor in a dataclass."""
        return f"{to_identifier(self.element.title)}"


# DataElement|CompositeElement, mandatory, repeat, [repr]


@dataclass
class SegmentSpec:
    """Specification of a segment, as defined in an EDIFACT EDSD file."""

    tag: str
    title: str
    schema: list[SegmentCompositeElementUsage | SegmentDataElementUsage]
    description: str = ""
    url: str = ""

    def class_name(self) -> str:
        return to_class_name(self.title, postfix="Segment")  # type: ignore


class MessageSegmentUsage(NamedTuple):
    pos: str  # 5 chars
    element: SegmentSpec
    parent: "MessageGroupUsage | MessageSpec"
    description: str = ""

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as accessor in a dataclass."""
        return f"{to_identifier(self.element.title)}"


class MessageGroupUsage(NamedTuple):
    pos: str  # 5 chars
    title: str
    members: list[str]
    parent: "MessageGroupUsage | MessageSpec"
    schema: dict[str, "MessageSegmentUsage | MessageGroupUsage"]
    description: str = ""

    @property
    def identifier(self) -> str:
        """Returns a Python identifier that can be used as an accessor in a
        dataclass."""
        return to_identifier(self.title)


@dataclass
class MessageSpec:
    tag: str
    title: str
    description: str
    schema: dict[str, MessageSegmentUsage | MessageGroupUsage]
    source: str = ""
    url: str = ""
    stub: bool = False

    def class_name(self) -> str:
        return to_class_name(self.title)


# global lists, indexed by code/tag of element/segment/message
data_element_specs: dict[str, DataElementSpec] = {}
composite_specs: dict[str, CompositeElementSpec] = {}
segment_specs: dict[str, SegmentSpec] = {}
message_specs: dict[str, MessageSpec] = {}
source_specs: dict[str, str] = {}
