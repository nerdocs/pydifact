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
from typing import NamedTuple, Optional, Type, TypeAlias, TypeVar

from pydifact.constants import EDI_DEFAULT_VERSION
from pydifact.exceptions import ValidationError

allowed_alphanum_chars = set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*-./:()'&=+\"?,"
    "!_\\ "
)


def is_edifact_alphanum(s: str) -> bool:
    """Returns True if str contains only alphanumeric characters in the sense of
    EDIFACT.

    The set method is extremely fast, which takes precedence here over having
    "exotic" chars like
    """
    # https://service.gefeg.com/jwg1/Files/V41-9735-1.pdf - page 11
    return all(
        c.isalnum() or (c.isascii() and c.isprintable() and not c.isalnum()) for c in s
    )
    # return all(c in allowed_alphanum_chars for c in s)


def assert_a(s, length, message=""):
    """checks if s consists of only alphabetical characters, and has a given length."""
    assert str(s).isalpha(), message
    assert len(s) == int(length), message


def assert_a_max(s, length, message=""):
    """checks if s consists of only alphabetical characters, and has a given maximum length."""
    assert str(s).isalpha() or s == "", message
    assert len(s) <= int(length), message


def assert_n(s, length, message=""):
    """checks if s is numeric and has a given length."""
    assert int(s), message
    assert len(s) == int(length), message


def assert_n_max(s, length, message=""):
    """checks if s is numeric and has a given length."""
    assert int(s), message
    assert len(s) <= int(length), message


def assert_an(s, length, message=""):
    """checks if s is alphanumeric and has a given length."""
    assert is_edifact_alphanum(s), message
    assert len(s) == int(length), message


def assert_an_max(s, length, message=""):
    """checks if s is alphanumeric and has a given length."""
    assert is_edifact_alphanum(s), message
    assert len(s) <= int(length), message


def assert_format(s, fmt_str, message=""):
    assert re.match(fmt_str, s), message


class Code(NamedTuple):
    name: str
    description: str


DataElementProviderType: TypeAlias = Type["DataElementProvider"]


class DataElementProvider:
    code: str
    """A 4 digit numeric code"""

    repr: str
    """the constraint of the data element's value."""

    title: str
    """The human readable title of the data element."""

    description: str
    """A short description of the data element"""

    plugins = []

    def __init_subclass__(cls, **kwargs):
        if not "__omitted__" in cls.__dict__ or getattr(cls, "__omitted__") is False:
            DataElementProvider.plugins.append(cls)

    def validate(self, mandatory: bool = None, repr: str = None) -> None:
        """Plugin hook that validates the data element and returns `True` if valid.

        Raises:
           ValidationError if any error occurs."""


# TODO: test DataElement
class DataElement(DataElementProvider):
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

    codes = {}
    """A possible dict of codes that can be used for validation"""

    def __init__(self, value: str):
        self.plugins = None
        self.value = value

    def validate(self, mandatory: bool = None, repr: str = None) -> None:
        """Validates the DataElement.

        Attributes:
            mandatory (bool): overrides the DataElement's default `mandatory` status
            repr (str): The data structure representation and length constraints

        Raises:
            ValidationError if validation fails.
        """
        if mandatory is True and not self.value:
            raise ValidationError(f"{self.__class__.__name__} must not be empty.")

        try:
            r = repr or self.repr
            tag_name = f"Tag {self.code} ({self.title})"
            if r[0] == "a":
                if r[1] == "n":
                    if r[2:4] == "..":
                        assert_an_max(
                            self.value,
                            r[4:],
                            f"{tag_name} "
                            f"must have max. {r[4:]} alphanumeric characters. Current value: "
                            f"'{self.value}'",
                        )
                    else:
                        assert_an(
                            self.value,
                            r[2:],
                            f"{tag_name} must have exactly "
                            f"{r[2:]} alphanumeric characters. Current value: "
                            f"'{self.value}'",
                        )
                else:
                    if r[1:2] == "..":
                        assert_a_max(
                            self.value,
                            r[3:],
                            message=f"{tag_name} "
                            f"must have max. {r[3:]} alphabetic characters. Current value: "
                            f"'{self.value}'",
                        ),
                    else:
                        assert_a(
                            self.value,
                            r[1:],
                            message=f"{tag_name} "
                            f"must have exactly {r[1:]} alphabetic characters. Current value: "
                            f"'{self.value}'",
                        )
            elif r[0] == "n":
                assert_n(
                    self.value,
                    r[1:],
                    message=f"{tag_name} must "
                    f"be numeric and must have {r[1:]} digits. Current value: "
                    f"'{self.value}'",
                )
            if self.codes and not self.value in self.codes:
                warnings.warn(
                    f"'{self.value}' is not a valid value of '{self.code}: {self.title}'.",
                    category=SyntaxWarning,
                )
        except AssertionError as e:
            raise ValidationError(e)


T = TypeVar("T", bound="CompositeDataElement")


# TODO: test CompositeDataElement
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

    schema: list[tuple[type(DataElement), str, str]]

    def __init__(self, elements: list[DataElement]):
        self.elements = elements if not isinstance(elements, str) else [elements]

    def validate(self, mandatory: bool = None, repeat: int = None) -> None:
        """Validates the CompositeDataElement.

        Attributes:
            mandatory (bool): If `True`, the element's default `mandatory` value is
                overridden. If `False`, the default value of the `DataElement`
                definition is used.
            repeat: The maximum number of times this composite data element is allowed to occur in this segment.
                A value of 1 means it can only appear once, while a value greater than 1 allows multiple occurrences
                up to that limit.
        """
        if mandatory and not self.elements:
            raise ValidationError(f"{self.__class__.__name__} must not be empty.")
        # TODO implement repeat
        # walk through all elements and check them against the schema
        for index, value in enumerate(self.elements):
            current_schema = self.schema[index]
            TemplateClass = current_schema[0]
            if len(current_schema) > 1:
                if not mandatory:
                    # If mandatory is not set, use the default value from the schema,
                    # or assume True if not set.
                    mandatory = (
                        (current_schema[1] == "M") if len(current_schema) > 1 else True
                    )
                # If data structure representation is not overridden, use
                # the default value from the schema
            if len(current_schema) > 2:
                data_struct_representation = current_schema[2]
            else:
                data_struct_representation = getattr(TemplateClass, "repr", None)
            if mandatory:
                # FIXME: even if not mandatory, but present, validation should be done.
                TemplateClass(value).validate(
                    mandatory=mandatory, repr=data_struct_representation
                )


# TODO: DataElementFactory is not used ATM
class DataElementFactory:
    """A factory for creating DataElement instances."""

    @staticmethod
    def create_data_element(
        code: str,
        value: Optional[str] = None,
        validate: bool = True,
        version: Optional[int] = EDI_DEFAULT_VERSION,
    ) -> DataElement:
        """Create a new instance of a DataElement

        Parameters:
            code: The code of the DataElement
            value: The data for this segment
            validate: bool if True, the created element should be validated
                before return
            version: The version of the EDI standard this element is based on
                (default: 4)
        """
        for Plugin in DataElementProvider.plugins:
            if (
                getattr(Plugin, "code", "") == code
                and getattr(Plugin, "version") == version
            ):
                s = Plugin(code, value)
                break
        else:
            # we don't support this kind of EDIFACT DataElement (yet), so
            # just create a generic DataElement()
            s = DataElement(value)
            s.code = "0000"  # unknown code. TODO: maybe find something better as code

        if validate:
            if not s.validate():
                raise ValueError(f"DataElement ({code}) `{value}` is not valid.")
        return s


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
