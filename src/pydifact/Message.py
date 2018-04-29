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
from pydifact.Parser import Parser
from pydifact.Segments import Segment
from pydifact.Serializer import Serializer


class Message:
    """Represent an EDI message for both reading and writing."""

    def __init__(self):

        # The segments that make up this message
        self.segments = []

    @classmethod
    def from_file(cls, file: str):
        """Create an instance from a file.

        Raises FileNotFoundError if filename is not found.
        :param file: The full path to a file that contains an EDI message
        :rtype: static
        """

        message = open(file).read()
        return cls.from_str(message)

    @classmethod
    def from_str(cls, string: str):
        """Create a instance from a string.
        :param string: The EDI message content
        :rtype: static
        """

        segments = Parser().parse(string)
        return cls.from_segments(segments)

    @classmethod
    def from_segments(cls, segments: list) -> list:
        """Create a instance from an array of segments.
        :param segments: The segments of the message
        :type segments: Segment[]
        """

        # create a new instance of Message and return it
        # with the added segments
        return cls().add_segments(segments)

    def get_all_segments(self) -> list:
        """Get all the segments.
        :rtype: Segment[]
        """
        return self.segments

    def get_segments(self, name: str) -> list:
        """Get all the segments that match the requested name.
        :param name: The name of the segment to return
        :rtype: Segment[]
        """
        for segment in self.get_all_segments():
            if segment.tag == name:
                yield segment

    def get_segment(self, name: str) -> Segment or None:
        """Get the first segment that matches the requested name.

         :return: The requested segment, or None if not found
        :param name: The name of the segment to return
        """
        for segment in self.get_segments(name):
            return segment


    def add_segments(self, segments: list) -> 'Message':
        """Add multiple segments to the message.
        :param segments: The segments to add
        :type segments: Segment[]
        """
        for segment in segments:
            self.add_segment(segment)

        return self

    def add_segment(self, segment: Segment) -> 'Message':
        """Add a segment to the message.
        :param segment: The segment to add
        """
        self.segments.append(segment)
        return self

    def serialize(self) -> str:
        """Serialize all the segments added to this object."""
        return Serializer().serialize(self.get_all_segments())

    def __str__(self) -> str:
        """Allow the object to be serialized by casting to a string."""
        return self.serialize()
