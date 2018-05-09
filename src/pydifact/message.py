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
import collections

from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.serializer import Serializer
from pydifact.control import Characters
import codecs

class Message:
    """Represent an EDI message for both reading and writing."""

    def __init__(self):

        # The segments that make up this message
        self.segments = []

        # Flag whether the UNA header is present
        self.has_una_segment = False

    @classmethod
    def from_file(cls, file: str, encoding: str = 'iso8859-1') -> 'Message':
        """Create a Message instance from a file.

        Raises FileNotFoundError if filename is not found.
        :param encoding: an 
        :param file: The full path to a file that contains an EDI message
        :rtype: Message
        """

        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            message = f.read()
        return cls.from_str(message)

    @classmethod
    def from_str(cls, string: str) -> 'Message':
        """Create a Message instance from a string.
        :param string: The EDI message content
        :rtype: Message
        """
        segments = Parser().parse(string)

        return cls.from_segments(segments)

    @classmethod
    def from_segments(cls, segments: list or collections.Iterable) -> 'Message':
        """Create a new Message instance from a iterable list of segments.

        :param segments: The segments of the message
        :type segments: list/iterable of Segment
        :rtype Message
        """

        # create a new instance of Message and return it
        # with the added segments
        return cls().add_segments(segments)

    def get_segments(self, name: str) -> list:
        """Get all the segments that match the requested name.
        :param name: The name of the segment to return
        :rtype: list of Segment
        """
        for segment in self.segments:
            if segment.tag == name:
                yield segment

    def get_segment(self, name: str) -> Segment or None:
        """Get the first segment that matches the requested name.

         :return: The requested segment, or None if not found
        :param name: The name of the segment to return
        """
        for segment in self.get_segments(name):
            return segment

        return None

    def add_segments(self, segments: list or collections.Iterable) -> 'Message':
        """Add multiple segments to the message.

        :param segments: The segments to add
        :type segments: list or iterable of Segments
        """
        for segment in segments:
            self.add_segment(segment)

        return self

    def add_segment(self, segment: Segment) -> 'Message':
        """Append a segment to the message.

        :param segment: The segment to add
        """
        if segment.tag == "UNA":
            self.has_una_segment = True
        self.segments.append(segment)
        return self

    def serialize(self) -> str:
        """Serialize all the segments added to this object."""
        return Serializer().serialize(self.segments, self.has_una_segment)

    def __str__(self) -> str:
        """Allow the object to be serialized by casting to a string."""
        return self.serialize()
