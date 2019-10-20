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
from typing import List

from pydifact.control.characters import Characters
import re

from pydifact.segments import Segment


class Serializer:
    """Serialize a bunch of segments into an EDI message string."""

    def __init__(self, characters: Characters = None):
        super().__init__()
        if characters is None:
            characters = Characters()

        self.characters = characters

    def serialize(self, segments: List[Segment], with_una_header: bool = True) -> str:
        """Serialize all the passed segments.

        :param segments: A list of segments to serialize
        :param with_una_header: set to False if you want to skip the UNA segment in the output.
            Defaults to True.
        """

        message_parts = []

        # if there is no UNA header, and user requests one...
        if with_una_header and len(segments) > 0:
            # create an EDIFACT header
            message_parts = [
                "UNA",
                self.characters.component_separator,
                self.characters.data_separator,
                self.characters.decimal_point,
                self.characters.escape_character,
                self.characters.reserved_character,
                self.characters.segment_terminator,
            ]

        # iter through all segments
        for segment in segments:
            # skip the UNA segment as we already have written it if requested
            if segment.tag == "UNA":
                continue
            message_parts += [segment.tag]
            for element in segment.elements:
                message_parts += [self.characters.data_separator]
                if type(element) == list:
                    for nr, subelement in enumerate(element):
                        element[nr] = self.escape(subelement)
                    message_parts += [self.characters.component_separator.join(element)]
                else:
                    message_parts += [self.escape(element)]

            message_parts += [self.characters.segment_terminator]

        message = "".join(message_parts)
        return message

    def escape(self, string: str or None) -> str:
        """Escapes control characters.

        :param string: The string to be escaped
        """

        if string is None:
            return ""
        assert type(string) == str, "%s is not a str, it is %s" % (string, type(string))

        characters = [
            self.characters.escape_character,
            self.characters.component_separator,
            self.characters.data_separator,
            self.characters.segment_terminator,
        ]
        replace_map = {}
        for character in characters:
            replace_map[character] = self.characters.escape_character + character

        # Thanks to "Bor González Usach" for this wonderful piece of code:
        # https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
        substrs = sorted(replace_map, key=len, reverse=True)
        regexp = re.compile("|".join(map(re.escape, substrs)))

        return regexp.sub(lambda match: replace_map[match.group(0)], string)
