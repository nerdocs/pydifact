"""
This file contains common used classes described in the EDIFACT syntax.

There are multiple versions (1-4) of the EDIFACT standard, and each differ slightly.
As one project will probably never use more than one syntax version simultaneously,
it is splitted into 4 different python files, each which could be imported using

    from pydifact.syntax.v[1..4] import ...

herby providing the same structure.
"""

import re
import warnings
from typing import NamedTuple, Type, TypeAlias, TypeVar

from pydifact.constants import M
from pydifact.exceptions import ValidationError

allowed_alphanum_chars = set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*-./:()'&=+\"?,!_\\ "
)


def is_edifact_alphanum(s: str) -> bool:
    """Returns True if str contains only alphanumeric characters in the sense of
    EDIFACT.

    See https://service.gefeg.com/jwg1/Files/V41-9735-1.pdf - page 11
    """
    return all(
        c.isalnum() or (c.isascii() and c.isprintable() and not c.isalnum()) for c in s
    )


# ISO 9735-1, 10.1.2.2: optional leading minus sign, digits, and at most one
# decimal mark with at least one digit on each side. The decimal mark is defined
# by the UNA (default ","), but "." is common in the wild, so both are accepted.
NUMERIC_RE = re.compile(r"-?[0-9]+(?:[.,][0-9]+)?")

# data structure representation: character type, optional ".." for variable
# length, and the (maximum) length. Examples: "a4", "an1", "an..35", "n..6".
_REPR_RE = re.compile(r"(an|a|n)(\.\.)?([0-9]+)")


def validate_repr(value: str, repr: str, name: str = "") -> None:
    """Checks `value` against a data structure representation like "an..35".

    Args:
        value: The string to check.
        repr: The representation: `a`/`n`/`an` followed by an exact length
            (`a4`) or `..` and a maximum length (`an..35`).
        name: Element name used in the error message.

    Raises:
        ValidationError: if `value` does not conform to `repr`.
        ValueError: if `repr` itself is malformed.
    """
    match = _REPR_RE.fullmatch(repr)
    if match is None:
        raise ValueError(f"Invalid data structure representation: '{repr}'")
    char_type, variable, length_str = match.groups()
    length = int(length_str)
    value_length = len(value)

    if char_type == "a":
        # letters and spaces, but no digits
        if not all(c.isalpha() or c == " " for c in value):
            raise ValidationError(
                f"{name} must contain alphabetic characters only. "
                f"Current value: '{value}'"
            )
    elif char_type == "n":
        if not NUMERIC_RE.fullmatch(value):
            raise ValidationError(f"{name} must be numeric. Current value: '{value}'")
        # sign and decimal mark do not count towards the length
        value_length = sum(c.isdigit() for c in value)
    elif not is_edifact_alphanum(value):
        raise ValidationError(
            f"{name} must contain alphanumeric characters only. "
            f"Current value: '{value}'"
        )

    if variable:
        if value_length > length:
            raise ValidationError(
                f"{name} must have max. {length} characters. Current value: '{value}'"
            )
    elif value_length != length:
        raise ValidationError(
            f"{name} must have exactly {length} characters. Current value: '{value}'"
        )


class Code(NamedTuple):
    name: str
    description: str


class DataElement:
    """Basic EDIFACT service code.

    Subclass this class to create custom service codes.

    Attributes:
        value (str): The service code (0001, 0002, 0325,...) as a string.
        repr (str): The data structure representation and length constraints:
            * a = Alphabetic characters only
            * n = Numeric characters only
            * an = Alphanumeric (both letters and numbers)
            * x = Variable length, exactly x characters
            * ..x = Variable length, up to x characters

            Examples: `a1`, `an3`, `a..3`, `an..6`
    """

    __omitted__ = True
    code: str
    """A 4 digit numeric code"""

    repr: str = ""
    """the constraint of the data element's value."""

    title: str = ""
    """The human readable title of the data element."""

    description: str = ""
    """A short description of the data element"""

    codes: dict[str, dict[str, str]] = {}
    """A possible dict of codes that can be used for validation"""

    def __init__(self, value: str):
        self.value = value

    def validate(self, mandatory: bool = False, repr: str | None = None) -> None:
        """Validates the DataElement.

        An empty value is only an error if the element is mandatory; a present
        value is always checked against the representation.

        Attributes:
            mandatory (bool): whether the element must not be empty
            repr (str): The data structure representation and length constraints;
                overrides the class' `repr` if given.

        Raises:
            ValidationError if validation fails.
        """
        if not self.value:
            if mandatory:
                raise ValidationError(f"{self.__class__.__name__} must not be empty.")
            return

        r = repr or self.repr
        if r:
            validate_repr(self.value, r, f"Tag {self.code} ({self.title})")
        if self.codes and self.value not in self.codes:
            warnings.warn(
                f"'{self.value}' is not a valid value of '{self.code}: {self.title}'.",
                category=SyntaxWarning,
            )


T = TypeVar("T", bound="CompositeDataElement")

CompositeSchemaEntry: TypeAlias = tuple[type[DataElement], str, str]
"""One entry of a `CompositeDataElement.schema`: the `DataElement` class, its
M(andatory)/C(onditional) flag and the data structure representation."""


class CompositeDataElement:
    code: str
    """A structured representation of a composite data element.
    
    A `CompositeDataElement` provides a schema which is a list of tuples, where each tuple
    represents a `DataElement` class, a M(andatory) or C(onditional) flag and a 
    representation of the data structure in a specific format.
    The original description is written like this:
    
    ```
    POS TAG  Name                             S R Repr. 
    010 S001 SYNTAX IDENTIFIER                M 1       
        0001 Syntax identifier                M   a4
        0002 Syntax version number            M   an1
        0080 Service code list dir. vers. nr. C   an..6
        0133 Character encoding, coded        C   an..3
    ...
    ```        

    So the schema is converted to python code like this:
    
    ```python
    schema = [
        (SyntaxIdentifier, M, "a4"),
        (SyntaxVersionNumber, M, "an1"),
        (...)
    ]
    ```
    
    Note that  only `CompositeDataElement`s have a "repeat" attribute, `DataElement`s 
    haven't.
    """

    schema: list[CompositeSchemaEntry]

    def __init__(self, elements: str | list[str]):
        self.elements = elements if not isinstance(elements, str) else [elements]

    def validate(self, mandatory: bool = False, repeat: int | None = None) -> None:
        """Validates the CompositeDataElement.

        Each component is checked against its schema entry: the M/C flag decides
        whether it may be empty, the representation constrains its value.

        Attributes:
            mandatory (bool): whether the composite must not be empty
            repeat: The maximum number of times this composite data element is allowed to occur in this segment.
                A value of 1 means it can only appear once, while a value greater than 1 allows multiple occurrences
                up to that limit.

        Raises:
            ValidationError if validation fails.
        """
        if not any(self.elements):
            if mandatory:
                raise ValidationError(f"{self.__class__.__name__} must not be empty.")
            return
        if len(self.elements) > len(self.schema):
            raise ValidationError(
                f"{self.__class__.__name__}: Too many components. Expected at most "
                f"{len(self.schema)}, got {len(self.elements)}: {self.elements}"
            )
        # TODO implement repeat
        for index, (TemplateClass, flag, repr) in enumerate(self.schema):
            value = self.elements[index] if index < len(self.elements) else ""
            TemplateClass(value).validate(mandatory=flag == M, repr=repr)


SegmentSchemaEntry: TypeAlias = (
    tuple[type[CompositeDataElement | DataElement], str, int]
    | tuple[type[CompositeDataElement | DataElement], str, int, str]
)
"""One entry of a `Segment.schema`: the element class, its M(andatory)/C(onditional)
flag, the maximum repeat count and optionally a representation that overrides the
element's default `repr`."""


# we provide the SyntaxVersionNumber here, as it does not make sense to include old
# ones. We have to decide anyway which version we support, so we need the newest list.


class SyntaxVersionNumber(DataElement):
    code = "0002"
    repr = "an1"
    title = "Syntax version number"
    codes = {
        "1": {
            "title": "Version 1",
            "description": "ISO 9735:1988.",
        },
        "2": {
            "title": "Version 2",
            "description": "ISO 9735:1988 (amended and reprinted in 1990).",
        },
        "3": {
            "title": "Version 3",
            "description": "ISO 9735:1988 and ISO 9735: 1988 / Amendment 1: 1992",
        },
        "4": {
            "title": "Version 4",
            "description": "ISO 9735:1998 (all parts)",
        },
    }
