#    pydifact - a python edifact library
#    Copyright (C) 2017-2018  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


class SegmentInterface:

    @property
    def tag(self) -> str:
        """Get the code/tag of this segment."""

    # TODO: make this more pythonic: a property would suffice
    def get_all_elements(self) -> list:
        """Get all the elements from the segment."""

    # TODO: make this more pythonic: iterable!
    def get_element(self, key: int) -> list or None:
        """Get an element from the segment."""


class AbstractSegment(SegmentInterface):
    """Represent a segment of an EDI message."""

    def __init__(self, code: str, *elements: tuple or list):
        """Create a new instance.
        :param str code: The code/tag of the segment.
        :param list elements: The data elements for this segment, as list.
        """
        assert type(code) == str
        self._code = code

        """The data elements for this segment.
        this is a tuple (due to the fact that python creates a tuple
        when passing a variable arguments list to a method)
        """
        self.elements = elements

    @property
    def tag(self) -> str:
        """Get the code of this segment."""
        return str(self._code)

    def get_all_elements(self) -> list:
        """Get all the elements from the segment."""
        return list(self.elements)

    def get_element(self, key: int) -> list or None:
        """Get an element from the segment.
        :param key The element to get
        :return the element, or None, if the key is out of range.
        """
        try:
            return self.elements[key]
        except IndexError:
            return

    def __str__(self) -> str:
        """Returns the Segment in Python list printout"""
        return '\'{}\' EDI segment'.format(self.tag)

    def __repr__(self) -> str:
        return self.tag + " segment: " + str(self.get_all_elements())

    def __eq__(self, other) -> bool:
        return self.get_all_elements() == other.get_all_elements()


class Segment(AbstractSegment):
    """Represent a segment of an EDI message."""


class FactoryInterface:
    """Factory for producing segments."""

    def create_segment(self, characters: str, name: str, *elements: tuple) -> SegmentInterface:
        """Create a new instance of the relevant class type.

        :param characters: The control characters
        :param name: The name of the segment
        :param elements: The data elements for this segment
        """
        raise NotImplementedError


class Factory(FactoryInterface):
    """Factory for producing segments."""

    def create_segment(self, characters: str, name: str, *elements: tuple) -> SegmentInterface:
        """Create a new Segment instance."""
        return Segment(name, elements)
