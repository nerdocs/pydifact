# Pydifact - a python edifact library
#
# Copyright (c) 2017-2024 Christian González
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

from collections.abc import Iterator

from pydifact.exceptions import EDISyntaxError
from pydifact.tokenizer import Tokenizer
from pydifact.token import Token
from pydifact.segments import Element, Elements, Segment, SegmentFactory
from pydifact.control import Characters


class Parser:
    """Parse EDI messages into a list of segments.

    Parameters:
        factory: The SegmentFactory to use for creating segments.
            (default: SegmentFactory())
        characters: The control characters to use. (default: Characters())
        version: The EDI version to use (default: 4)
    """

    def __init__(
        self,
        factory: SegmentFactory | None = None,
        characters: Characters | None = None,
        version: int | None = None,
    ) -> None:
        self.factory = factory or SegmentFactory()
        self.characters = characters or Characters()
        self.version = version or 4

    def parse(
        self, message: str, characters: Characters | None = None
    ) -> Iterator[Segment]:
        """Parse the message into a list of segments.

        :param characters: the control characters to use, if there is no
                UNA segment present
        :param message: The EDI message
        :rtype:
        """

        # If there is a UNA, take the following 6 characters
        # unconditionally, strip them, and make control Characters()
        # for further parsing

        # If it starts by UNA
        una_pattern = "UNA"
        if message.startswith(una_pattern):
            idx_una = 0
        # Otherwise we look for UNA, so to avoid finding "lorem ipsum UNA lorem ipsum" we look for the segment separator following by UNA.
        else:
            una_pattern = "'UNA"
            idx_una = message.find(una_pattern)
        una_found = idx_una != -1

        if una_found:
            idx_begin = idx_una + len(una_pattern)
            idx_end = idx_begin + 6
            characters = Characters.from_str(f"UNA{message[idx_begin: idx_end]}")

            # remove the UNA segment from the string,
            # ignore everything before UNA because it should be the first segment if una_found.
            message = message[idx_end:].lstrip("\r\n")

        else:
            # if no UNA header present, use default control characters
            # given on call take precedence over the stored defaults.
            if characters is None:
                characters = self.characters

        tokenizer = Tokenizer()
        return self.convert_tokens_to_segments(
            tokenizer.get_tokens(message, characters),
            characters,
            with_una=una_found,
        )

    @staticmethod
    def get_control_characters(
        message: str, characters: Characters | None = None
    ) -> Characters | None:
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

    def convert_tokens_to_segments(
        self, tokens: Iterator[Token], characters: Characters, with_una: bool = False
    ) -> Iterator[Segment]:
        """Convert the tokenized message into an array of segments.
        :param tokens: The tokens that make up the message
        :param characters: the control characters to use
        :param with_una: whether the UNA segment should be included
        :type tokens: list of Token
        :rtype list of Segment
        """

        raw_segments: list[Elements] = []
        current_segment: Elements = []
        data_element: list[str] = []
        data_element_value: Element
        in_segment = False
        empty_component_counter = 0

        if with_una:
            yield self.factory.create_segment("UNA", str(characters))

        for token in tokens:
            # If we're in the middle of a segment, check if we've reached the end
            if in_segment:
                if token.type == Token.Type.TERMINATOR:
                    in_segment = False
                    if len(data_element) == 0:  # empty element
                        data_element_value = ""
                    elif len(data_element) == 1:
                        # use a str instead of a list
                        data_element_value = data_element[0]
                    else:
                        data_element_value = data_element

                    current_segment.append(data_element_value)
                    data_element = []
                    continue

            # If we're not in a segment, then start a new empty one now
            # and add it to the list. Also create a new empty data element,
            # because if the next token is a DATA_SEPARATOR, at least we have
            # an empty string to save into the segment then.
            else:
                current_segment = []
                raw_segments.append(current_segment)
                data_element = []
                empty_component_counter = 0
                in_segment = True

            # Whenever we reach a data separator (+), we add the currently
            # collected data element to the current segment and reset the
            # data_element to an empty list []
            if token.type == Token.Type.DATA_SEPARATOR:
                if len(data_element) == 0:  # empty element
                    data_element_value = ""
                elif len(data_element) == 1:
                    data_element_value = data_element[0]
                else:
                    data_element_value = data_element

                current_segment.append(data_element_value)

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
                (
                    empty_component_counter
                    if data_element
                    else empty_component_counter + 1
                ),
            ):
                data_element.append("")

            data_element.append(token.value)
            empty_component_counter = 0
            continue

        for segment in raw_segments:
            name = segment.pop(0)
            if with_una and name == "UNA":
                # We found another UNA segment.
                # This is not in the specs, so raise an error
                raise EDISyntaxError("There are not multiple UNA segments allowed.")
            if name == "UNB":
                self.version = int(segment[0][1])
                print("found edifact version", self.version)
            yield self.factory.create_segment(name, *segment, version=self.version)
