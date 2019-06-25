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


class Segment:
    """Represent a segment of an EDI message."""

    def __init__(self, tag: str, *elements):
        """Create a new instance.
        :param str tag: The code/tag of the segment.
        :param list elements: The data elements for this segment, as list.
        """
        assert type(tag) == str
        self.tag = tag

        """The data elements for this segment.
        this is converted to a list (due to the fact that python creates a tuple
        when passing a variable arguments list to a method)
        """
        self.elements = list(elements)

    def __str__(self) -> str:
        """Returns the Segment in Python list printout"""
        return "'{}' EDI segment: {}".format(self.tag, str(self.elements))

    def __repr__(self) -> str:
        return self.tag + " segment: " + str(self.elements)

    def __eq__(self, other) -> bool:
        return type(self) == type(other) and list(self.elements) == list(other.elements)


class SegmentFactory:
    """Factory for producing segments."""

    def create_segment(self, characters: str, name: str, *elements: list) -> Segment:
        """Create a new instance of the relevant class type.

        :param characters: The control characters
        :param name: The name of the segment
        :param elements: The data elements for this segment
        """
        return Segment(name, *elements)
