#    pydifact - a python edifact library
#    Copyright (C) 2017  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


class Segment:
    """Represent a segment of an EDI message."""

    def __init__(self, name: str, *elements: tuple):
        """Create a new instance.
        :param str name: The name of the segment.
        :param list elements: The data elements for this segment, as list.
        """

        # The name of the segment.
        # TODO: rename into "tag"
        self. name = name

        """The data elements for this segment.
        this is a tuple (due to the fact that python creates a tuple
        when passing a variable arguments list to a method)
        """
        self.elements = elements

    def __str__(self) -> str:
        return self.getName()

    # TODO: rename into get_tag"
    def getName(self) -> str:
        """Get the name of this segment."""

        return self.name

    def getAllElements(self) -> list:
        """Get all the elements from the segment."""

        return list(self.elements)

    def getElement(self, key: int) -> list or None:
        """Get an element from the segment.
        :param int key The element to get
        :return the element, or None, if the key is out of range.
        """
        try:
            return self.elements[key]
        except IndexError:
            return

    def __eq__(self, other):
        return self.getAllElements() == other.getAllElements()
