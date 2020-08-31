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
from typing import Optional, Generator, Any

from pydifact.tokenizer import Tokenizer
from pydifact.token import Token
from pydifact.segments import Segment, SegmentFactory
from pydifact.control import Characters


class Parser:
    """Parse EDI messages into a list of segments."""

    def __init__(self, factory: SegmentFactory = None):
        if factory is None:
            factory = SegmentFactory()

        self.factory = factory
        self.characters = Characters()

    def parse(
        self, message: str, characters: Characters = None
    ) -> Generator[Segment, Any, None]:
        """Parse the message into a list of segments.

        :param characters: the control characters to use, if there is no
                UNA segment present
        :param message: The EDI message
        :rtype:
        """

        # If there is a UNA, take the following 6 characters
        # unconditionally, save them, strip them, and make control Characters()
        # for further parsing
        if message[0:3] == "UNA":
            self.characters = Characters.from_str("UNA" + message[3:9])

            # remove the UNA segment from the string
            message = message[9:].lstrip("\r\n")

        else:
            # if no UNA header present, use default control characters
            if characters is not None:
                self.characters = characters

        tokenizer = Tokenizer()
        return self.convert_tokens_to_segments(
            tokenizer.get_tokens(message, self.characters), self.characters
        )

    @staticmethod
    def get_control_characters(
        message: str, characters: Characters = None
    ) -> Optional[Characters]:
        """Read the UNA segment from the passed string and extract/store the control characters from it.

        :param message: a valid EDI message string, or UNA segment string,
                        to extract the control characters from.
        :param characters: the control characters to use, if none found in
                           the message. Default: ":+,? '"
        :return: the control characters
        """

        if not characters:
            characters = Characters()

        # First, try to read the UNA segment ("Service String Advice",
        # conditional). This segment and the UNB segment (Interchange Header)
        # must always be written in ASCII, even if after the BGM the files
        # continues with cyrillic or UTF-16.

        # If it does not exist, return a default.
        if not message[:3] == "UNA":
            return characters

        # Get the character definitions
        chars = message[3:9]
        characters.is_extracted_from_message = True

        characters.component_separator = chars[0]
        characters.data_separator = chars[1]
        characters.decimal_point = chars[2]
        characters.escape_character = chars[3]
        characters.reserved_character = chars[4]
        characters.segment_terminator = chars[5]

        return characters

    def convert_tokens_to_segments(self, tokens: list, characters: Characters):
        """Convert the tokenized message into an array of segments.
        :param with_una: whether the UNA segment should be included
        :param tokens: The tokens that make up the message
        :param characters: the control characters to use
        :type tokens: list of Token
        :rtype list of Segment
        """

        segments = []
        current_segment = []
        data_element = None
        in_segment = False
        empty_component_counter = 0

        for token in tokens:

            # If we're in the middle of a segment, check if we've reached the end
            if in_segment:

                if token.type == Token.Type.TERMINATOR:
                    in_segment = False
                    if len(data_element) == 0:  # empty element
                        data_element = ""
                    if len(data_element) == 1:
                        # use a str instead of a list
                        data_element = data_element[0]

                    current_segment.append(data_element)
                    data_element = []
                    continue

            # If we're not in a segment, then start a new empty one now
            # and add it to the list. Also create a new empty data element,
            # because if the next token is a DATA_SEPARATOR, at least we have
            # an empty string to save into the segment then.
            else:
                current_segment = []
                segments.append(current_segment)
                data_element = []
                in_segment = True

            # Whenever we reach a data separator (+), we add the currently
            # collected data element to the current segment and reset the
            # data_element to an empty list []
            if token.type == Token.Type.DATA_SEPARATOR:
                if len(data_element) == 0:  # empty element
                    data_element = ""
                elif len(data_element) == 1:
                    data_element = data_element[0]

                current_segment.append(data_element)

                data_element = []
                empty_component_counter = 0
                continue

            # Whenever we reach a component data separator (:), we know that
            # the whole data element is a composite, so increment the counter
            # this is especially needed when more than one component data
            # separators are in a row "23:::56"
            if token.type == Token.Type.COMPONENT_SEPARATOR:
                empty_component_counter += 1
                continue

            # here we can be sure that the token value is normal "content"
            # first backfill empty strings for skipped component data (:::)
            for i in range(
                1,
                empty_component_counter
                if data_element
                else empty_component_counter + 1,
            ):
                data_element.append("")

            data_element.append(token.value)
            empty_component_counter = 0
            continue

        self.factory.characters = characters
        for segment in segments:
            name = segment.pop(0)
            yield self.factory.create_segment(name, *segment)
