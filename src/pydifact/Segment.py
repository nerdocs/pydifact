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
    
    def __init__(self, name, elements=[]):
        """
        Create a new instance.
    
        :param string $name The name of the segment.
        :param array $elements The data elements for this segment.
        """
        # The name of the segment.
        self. name = name
        
        # The data elements for this segment.
        self.elements = elements
        

    def getName(self):
        """
        Get the name of this segment.
        :return string
        """
        return self.name


    def getAllElements(self):
        """
        Get all the elements from the segment.
        :return array
        """
        return self.elements


    def getElement(self, key):
        """
        Get an element from the segment.
        :param int key The element to get
        :return mixed
        """
        try:
            return self.elements[key]
        except IndexError:
            return

