# Pydifact - a python edifact library
#
# Copyright (c) 2017-2024 Christian González
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import warnings
import logging
from typing import overload
from functools import lru_cache
from pathlib import Path
import xml.etree.ElementTree as ET

from pydifact.constants import (
    EDI_DEFAULT_VERSION,
    M,
    EDI_DEFAULT_SYNTAX,
    Element,
    EDI_DEFAULT_DIRECTORY,
    service_segments,
)
from pydifact.exceptions import (
    ValidationError,
    MissingImplementationWarning,
    EDISyntaxError,
)
from pydifact.syntax.common import DataElement, CompositeDataElement

logger = logging.getLogger(__name__)


@lru_cache(maxsize=32)
def _load_segments_xml(directory: str) -> ET.Element:
    """Load and cache segments.xml from the specified directory.

    Args:
        directory: The directory name under pydifact.syntax (e.g., 'd00a', 'd96a')

    Returns:
        The root element of the parsed XML tree

    Raises:
        FileNotFoundError: If segments.xml cannot be found in the directory
        ET.ParseError: If the XML file cannot be parsed
    """
    # Get the path to the syntax directory
    syntax_path = Path(__file__).parent / "syntax" / directory / "segments.xml"

    if not syntax_path.exists():
        raise FileNotFoundError(f"segments.xml not found in directory: {directory}")

    tree = ET.parse(syntax_path)
    return tree.getroot()


class Segment:
    """Represents a low-level segment of an EDI interchange.

    This class is used internally. Real-world implementations of specialized should
    subclass Segment and provide
    the `tag` attribute and `validate()` method.
    """

    # tag is not a class attribute in this case, as each Segment instance could have another tag.
    __omitted__ = True
    plugins: list = []
    schema: list[tuple[type[CompositeDataElement | DataElement], str, int, str]] = []
    tag = ""
    elements = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "__omitted__" not in cls.__dict__ or getattr(cls, "__omitted__") is False:
            cls.plugins.append(cls)

    @overload
    def __init__(self, tag: str, *elements: Element): ...

    @overload
    def __init__(self, *elements: Element): ...

    def __init__(self, *args):
        """Create a new Segment instance.

        Params:
            tag: The code/tag of the segment. On Segment, must not be empty. On
                subclasses of Segment it can be omitted
            elements: The data elements for this segment, as (possibly empty) list.

        """
        # if there is no tag defined in the class itself, it MUST be passed as the first
        # argument.
        if not self.tag:
            if len(args) < 1:
                raise AttributeError(
                    f"{self}: A generic segment must provide a tag as first argument."
                )
            self.tag = args[0]

            self.elements = list(args[1:])
        else:
            self.elements = list(args)

        if not self.elements:
            warnings.warn(
                f"Segment {self.tag} is empty, and should be omitted completely.",
                category=SyntaxWarning,
            )
        # Validate segment tag is uppercase alphanumeric 3‑letter string
        if (
            not isinstance(self.tag, str)
            or not self.tag.isalnum()
            or len(self.tag) != 3
            or not self.tag.isupper()
        ):
            raise ValueError(
                f"Segment tag must be an uppercase 3-letter string, not '{self.tag}'."
            )

    def __str__(self) -> str:
        """Returns the user-readable text representation of this segment."""
        return f"'{self.tag}' EDI segment: {self.elements}"

    def __repr__(self) -> str:
        return f"{self.tag} segment: {str(self.elements)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return str(self) == other
        # FIXME the other way round too? isinstance(other, type(self))?
        return (
            isinstance(self, type(other))
            and self.tag == other.tag
            and list(self.elements) == list(other.elements)
        )

    def __getitem__(self, key: int) -> Element | None:
        """
        Retrieves an element from the list of elements based on the provided index.

        If the index is out of bounds, the method returns `Ǹone`.
        """
        return self.elements[key] if len(self.elements) > key else None

    def __setitem__(self, key: int, value: Element) -> None:
        self.elements[key] = value

    def validate(self, syntax_version: str = "", directory: str = "") -> None:
        """
        Segment validation against a given syntax version and EDIFACT directory.

        The Segment class is part of the lower level interfaces of pydifact.
        Args:
            syntax_version: The EDIFACT syntax version to validate against (e.g., 'D96A')
            directory: The directory name under pydifact.syntax (e.g., 'd00a', 'd96a')

        Raises:
            ValidationError, if the validation fails.
        """
        if directory:
            try:
                # load segments xml (or cache it)
                if self.tag in service_segments:
                    xml_root = _load_segments_xml(f"service/v{syntax_version}")
                else:
                    xml_root = _load_segments_xml(directory)

                # Find the segment definition in XML
                segment_def = xml_root.find(f".//segment[@id='{self.tag}']")

                if segment_def is None:
                    logger.warning(f"No definition found for segment {self.tag}")
                else:
                    # Validate against XML schema
                    xml_elements = segment_def.findall(".//element")

                    for index, element in enumerate(self.elements):
                        if index >= len(xml_elements):
                            raise ValidationError(
                                f"{self.tag}: Too many elements. Expected {len(xml_elements)}, "
                                f"got {len(self.elements)}"
                            )

                        xml_element = xml_elements[index]
                        is_mandatory = (
                            xml_element.get("mandatory", "false").lower() == "true"
                        )

                        if is_mandatory and (element is None or element == ""):
                            raise ValidationError(
                                f"{self.tag} Segment, pos. {index}: Mandatory element is missing"
                            )

            except FileNotFoundError:
                warnings.warn(
                    f"segments.xml not found for directory '{directory}'. "
                    f"Falling back to schema-based validation.",
                    category=MissingImplementationWarning,
                )
            except ET.ParseError as e:
                warnings.warn(
                    f"Failed to parse segments.xml: {e}. "
                    f"Falling back to schema-based validation.",
                    category=MissingImplementationWarning,
                )

        for index, element in enumerate(self.elements):
            # validation is only done in specific segments, not in generic "Segment"
            if self.__class__ is not Segment:
                # if there are codes defined, use them for validation
                if self.schema:
                    if index >= len(self.schema):
                        raise ValidationError(
                            f"{self.__class__.__name__}: odd element at position {index}: "
                            f"'{element}'"
                        )
                    schema = self.schema[index]
                    template_cls = schema[0]
                    mandatory = (schema[1] == M) if len(schema) > 1 else True
                    repeat = schema[2] if len(schema) > 2 else 1  # TODO implement
                    if len(schema) > 3:
                        repr = schema[3]
                    else:
                        repr = getattr(template_cls, "repr", None)

                    if mandatory:
                        try:
                            template_cls(element).validate(mandatory, repr)
                        except ValidationError as e:
                            raise ValidationError(
                                f"{self.tag} Segment, pos. {index}: {e}"
                            )
                else:
                    warnings.warn(
                        f"{self.__class__.__name__} does not "
                        f"implement codes for element {index}: '{element}'",
                        category=MissingImplementationWarning,
                    )


class SegmentFactory:
    """Factory for producing segments."""

    @staticmethod
    def create_segment(
        name: str,
        *elements: Element,
        validate: bool = True,
        version: str = EDI_DEFAULT_VERSION,
        directory: str = EDI_DEFAULT_DIRECTORY,
        syntax_identifier: str = EDI_DEFAULT_SYNTAX,  # unused yet
    ) -> Segment:
        """Create a new instance of the relevant class type.

        Parameters:
            name: The name of the segment
            elements: The data elements for this segment
            validate: bool if True, the created segment is validated before return
            version: The version of the EDI standard this segment is based on
                    (default: 4)
        """
        # Basic segment type validation is done here.
        # The more special validation must be done in the corresponding Segment

        if not name:
            raise EDISyntaxError("The tag of a segment must not be empty.")

        if not isinstance(name, str):
            raise EDISyntaxError(
                f"The tag name of a segment must be a str, but is a {type(name)}: {name}"
            )
        if not name.isalnum():
            raise EDISyntaxError(
                f"Tag '{name}': A tag name must only contain alphanumeric characters."
            )
        # TODO: don't iterate over plugins, use a dict to find plugins faster
        for Plugin in Segment.plugins:
            if (
                getattr(Plugin, "tag", "") == name
                and getattr(Plugin, "version", EDI_DEFAULT_VERSION) == version
            ):
                # use specific Segment subclass for this tag
                segment = Plugin(*elements)
                break
        else:
            # we don't support this kind of EDIFACT segment (yet), so
            # just create a generic Segment()
            segment = Segment(name, *elements)

        if validate:
            segment.validate(version, directory)

        return segment
