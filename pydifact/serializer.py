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
from typing import List, Optional

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
        self.replace_map = characters.escaped_syntax_dic

        # Thanks to "Bor González Usach" for this wonderful piece of code:
        # https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
        substrs = sorted(self.replace_map, key=len, reverse=True)
        self.regexp = re.compile("|".join(map(re.escape, substrs)))

    def serialize(
        self, segments: List[Segment], with_una_header: bool = True, break_lines=False
    ) -> str:
        """Serialize all the passed segments.

        :param segments: A list of segments to serialize
        :param with_una_header: includes/adds an UNA header if set to True (=default)
            If the segments list contains a UNA header, it is taken, else the default character set
            is created.
        :param break_lines: if True, insert line break after each segment terminator.
        """
        collection_parts = []

        # first, check if UNA header is wanted.
        if with_una_header:
            if not segments:
                return self.characters.service_string_advice
            else:
                collection_parts += self.characters.service_string_advice

        else:
            # no una header wanted!
            if not segments:
                return ""

        # iter through all segments
        for segment in segments:
            # skip the UNA segment as we already have written it if requested
            if segment.tag == "UNA":
                continue
            collection_parts += segment.tag
            for element in segment.elements:
                collection_parts += self.characters.data_separator
                if type(element) == list:
                    element = (self.escape(subelement) for subelement in element)
                    collection_parts += self.characters.component_separator.join(
                        element
                    )

                else:
                    collection_parts += self.escape(element)

            collection_parts += self.characters.segment_terminator
            if break_lines:
                collection_parts += "\n"

        collection = "".join(collection_parts)
        return collection

    def escape(self, string: Optional[str]) -> str:
        """Escapes control characters.

        :param string: The string to be escaped
        """

        if string is None:
            return ""
        assert type(string) == str, "%s is not a str, it is %s" % (string, type(string))

        return self.regexp.sub(lambda match: self.replace_map[match.group(0)], string)
