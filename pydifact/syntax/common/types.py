import warnings
from typing import NamedTuple

from pydifact.constants import M
from pydifact.exceptions import ValidationError
from pydifact.utils import assert_a, assert_a_max, assert_n, assert_an, assert_an_max


class Code(NamedTuple):
    name: str
    description: str


class DataElement:
    """Basic EDIFACT service code.

    Subclass this class to create custom service codes.

    Attributes:
        value (str): The service code (0001, 0002, 0325, ...) as a string.
        repr (str): The data structure representation and length constraints:
            * a = Alphabetic characters only
            * n = Numeric characters only
            * an = Alphanumeric (both letters and numbers)
            * x = Variable length, exactly x characters
            * ..x = Variable length, up to x characters

            Examples: `a1`, `an3`, `a..3`, `an..6`
    """

    # TODO: test DataElement

    __omitted__ = True
    code: str
    """A 4 digit numeric code"""

    repr: str
    """the constraint of the data element's value."""

    title: str
    """The human readable title of the data element."""

    description: str
    """A short description of the data element"""

    codes: dict[str, Code] = {}
    """A possible dict of codes that can be used for validation"""

    def __init__(self, value: str):
        self.value = value

    def validate(self, mandatory: bool | None = None, repr: str | None = None) -> None:
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
            if self.codes and self.value not in self.codes:
                warnings.warn(
                    f"'{self.value}' is not a valid value of '{self.code}: {self.title}'.",
                    category=SyntaxWarning,
                )
        except AssertionError as e:
            raise ValidationError(e)


DataElementType = type[DataElement]
CompositeDataElementType = type["CompositeDataElement"]
DataElementSchemaEntry = tuple[DataElementType, bool, str]
CompositeSchemaEntry = tuple[CompositeDataElementType, bool, int]
CompositeSchemaEntryList = list[DataElementSchemaEntry]
DataElementSchemaList = list[DataElementSchemaEntry]


SegmentSchema = dict[str, CompositeSchemaEntry | DataElementSchemaEntry]


class CompositeDataElement:
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

    # TODO: test CompositeDataElement

    code: str
    schema: CompositeSchemaEntryList

    def __init__(self, elements: list[DataElement]):
        self.elements = elements if not isinstance(elements, str) else [elements]

    def validate(self, mandatory: bool, repeat: int) -> None:
        """Validates the CompositeDataElement.

        Attributes:
            mandatory (bool): If `True`, the element's default `mandatory` value is
                overridden. If `False`, the default value of the `DataElement`
                definition is used.
            repeat: The maximum number of times this composite data element is allowed
                to   occur in this segment. A value of 1 means it can only appear
                once, while a value greater than 1 allows multiple occurrences up to
                that limit.
        """
        if mandatory and not self.elements:
            raise ValidationError(f"{self.__class__.__name__} must not be empty.")
        # TODO: implement repeat
        # walk through all elements and check them against the schema
        for index, value in enumerate(self.elements):
            current_schema = self.schema[index]
            TemplateClass: DataElementType = current_schema[0]
            # If data structure representation is not overridden, use
            # the default value of the DataElement class.
            data_struct_representation = getattr(TemplateClass, "repr", None)
            if len(current_schema) > 1:
                if mandatory is None:
                    # If mandatory is not set, use the default value from the schema,
                    # or assume True if not set.
                    mandatory = current_schema[1] == M
            elif len(current_schema) > 2:
                # override representation if set in schema
                data_struct_representation = current_schema[2]

            if mandatory:
                # FIXME: even if not mandatory, but present, validation should be done.
                # FIXME: casting here is doen wrong. value is a DataElement already.
                TemplateClass(value).validate(
                    mandatory=mandatory, repr=data_struct_representation
                )
