# Pydifact - a python edifact library
#
# Copyright (c) 2019 Christian González
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
from typing import Union, List

from pydifact.api import EDISyntaxError, PluginMount
from pydifact.control import Characters


class SegmentProvider(metaclass=PluginMount):
    """This is a plugin mount point for Segment plugins which represent a certain EDIFACT Segment.

    Classes implementing this PluginMount should provide the following attributes:
    """

    def __str__(self):
        """Returns the user readable text representation of this segment."""

    def validate(self) -> bool:
        """Validates the Segment."""


class Segment(SegmentProvider):
    """Represents a low-level segment of an EDI interchange.

    This class is used internally. read-world implementations of specialized should subclass Segment and provide
    the `tag` and `validate` attributes.
    """

    # tag is not a class attribute in this case, as each Segment instance could have another tag.
    __omitted__ = True

    def __init__(self, tag: str, *elements: Union[str, List[str]]):
        """Create a new Segment instance.

        :param str tag: The code/tag of the segment. Must not be empty.
        :param list elements: The data elements for this segment, as (possibly empty) list.

        """
        self.tag = tag

        # The data elements for this segment.
        # this is converted to a list (due to the fact that python creates a tuple
        # when passing a variable arguments list to a method)
        self.elements = list(elements)

    def __str__(self) -> str:
        """Returns the Segment in Python list printout"""
        return "'{tag}' EDI segment: {elements}".format(
            tag=self.tag, elements=str(self.elements)
        )

    def __repr__(self) -> str:
        return "{} segment: {}".format(self.tag, str(self.elements))

    def __eq__(self, other) -> bool:
        # FIXME the other way round too? isinstance(other, type(self))?
        return (
            isinstance(self, type(other))
            and self.tag == other.tag
            and list(self.elements) == list(other.elements)
        )

    def __getitem__(self, key):
        return self.elements[key]

    def __setitem__(self, key, value):
        self.elements[key] = value

    def validate(self) -> bool:
        """
        Segment validation.

        The Segment class is part of the lower level interfaces of pydifact.
        So it assumes that the given parameters are correct, there is no validation done here.
        However, in segments derived from this class, there should be validation.

        :return: bool True if given tag and elements are a valid EDIFACT segment, False if not.
        """
        # FIXME: there should be a way of returning an error message - WHICH kind of validation failed.

        if not self.tag:
            return False
        return True


class SegmentFactory:
    """Factory for producing segments."""

    characters = None

    @staticmethod
    def create_segment(
        name: str, *elements: Union[str, List[str]], validate: bool = True
    ) -> Segment:
        """Create a new instance of the relevant class type.

        :param name: The name of the segment
        :param elements: The data elements for this segment
        :param validate: bool if True, the created segment is validated before return
        """
        if not SegmentFactory.characters:
            SegmentFactory.characters = Characters()

        # Basic segment type validation is done here.
        # The more special validation must be done in the corresponding Segment

        if not name:
            raise EDISyntaxError("The tag of a segment must not be empty.")

        if type(name) != str:
            raise EDISyntaxError(
                "The tag name of a segment must be a str, but is a {}: {}".format(
                    type(name), name
                )
            )

        if not name.isalnum():
            raise EDISyntaxError(
                "Tag '{}': A tag name must only contain alphanumeric characters.".format(
                    name
                )
            )

        for Plugin in SegmentProvider.plugins:
            if Plugin().tag == name:
                s = Plugin(name, *elements)
        else:
            # we don't support this kind of EDIFACT segment (yet), so
            # just create a generic Segment()
            s = Segment(name, *elements)

        if validate:
            if not s.validate():
                raise EDISyntaxError(
                    "could not create '{}' Segment. Validation failed.".format(name)
                )

        # FIXME: characters is not used!
        return Segment(name, *elements)
