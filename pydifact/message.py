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
        self.characters = Characters()

        # Flag whether the UNA header is present
        self.has_una_segment = False

    @classmethod
    def from_file(cls, file: str, encoding: str = "iso8859-1") -> "Message":
        """Create a Message instance from a file.

        Raises FileNotFoundError if filename is not found.
        :param encoding: an optional string which specifies the encoding. Default is "iso8859-1".
        :param file: The full path to a file that contains an EDI message.
        :rtype: Message
        """

        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            message = f.read()
        return cls.from_str(message)

    @classmethod
    def from_str(cls, string: str) -> "Message":
        """Create a Message instance from a string.
        :param string: The EDI message content
        :rtype: Message
        """
        segments = Parser().parse(string)

        return cls.from_segments(segments)

    @classmethod
    def from_segments(cls, segments: list or collections.Iterable) -> "Message":
        """Create a new Message instance from a iterable list of segments.

        :param segments: The segments of the message
        :type segments: list/iterable of Segment
        :rtype: Message
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

    def add_segments(self, segments: list or collections.Iterable) -> "Message":
        """Add multiple segments to the message.

        :param segments: The segments to add
        :type segments: list or iterable of Segments
        """
        for segment in segments:
            self.add_segment(segment)

        return self

    def add_segment(self, segment: Segment) -> "Message":
        """Append a segment to the message.

        :param segment: The segment to add
        """
        if segment.tag == "UNA":
            self.has_una_segment = True
            self.characters = Characters.from_str(segment.elements[0])
        self.segments.append(segment)
        return self

    def serialize(self) -> str:
        """Serialize all the segments added to this object."""
        return Serializer(self.characters).serialize(
            self.segments, self.has_una_segment
        )

    def __str__(self) -> str:
        """Allow the object to be serialized by casting to a string."""
        return self.serialize()
