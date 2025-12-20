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

from pydifact.constants import (
    EDI_DEFAULT_VERSION,
    EDI_DEFAULT_SYNTAX,
    Element,
    Elements,
    EDI_DEFAULT_DIRECTORY,
)
from pydifact.exceptions import EDISyntaxError
from pydifact.tokenizer import Tokenizer
from pydifact.token import Token
from pydifact.segments import Segment, SegmentFactory
from pydifact.control import Characters


class Parser:
    """Parse EDI messages into a list of segments.

    Parameters:
        factory: The SegmentFactory to use for creating segments.
            (default: SegmentFactory())
        characters: The control characters to use. (default: Characters())
        version: The EDI version to override. (default: from UNB header)
        directory: The directory to use for segments. (default: EDI_DEFAULT_DIRECTORY)
        syntax_identifier: The syntax identifier to use for segments. (default: from UNB header)
    """

    def __init__(
        self,
        factory: SegmentFactory | None = None,
        characters: Characters | None = None,
        version_override: str = "",
        directory: str = "",
        syntax_identifier: str = "",
    ) -> None:
        """Initializes parser with segment factory and control characters"""
        self.factory = factory or SegmentFactory()
        self.characters = characters or Characters()
        self.version = version_override or EDI_DEFAULT_VERSION
        self.directory = directory or EDI_DEFAULT_DIRECTORY
        self.syntax_identifier = syntax_identifier or EDI_DEFAULT_SYNTAX

    def parse(
        self,
        message: str,
        characters: Characters | None = None,
        directory: str = EDI_DEFAULT_DIRECTORY,
    ) -> Iterator[Segment]:
        """Parse the message into a list of segments.

        Args:
            message: The EDI message string to parse.
            characters: The control characters to use, if there is no
                UNA segment present. Defaults to None.
            directory: The directory to use for segments. Defaults to
                EDI_DEFAULT_DIRECTORY.

        Yields:
            Segment: Parsed segment objects from the EDI message.
        """

        # If there is a UNA segment, take the following 6 characters
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
            # if no UNA header present, the default control characters
            # given on call take precedence over the stored defaults.
            if characters is None:
                characters = self.characters

        # if UNA is available, yield the UNA segment first, even before tokenizing
        if una_found:
            yield self.factory.create_segment("UNA", str(characters))

        tokenizer = Tokenizer()
        raw_segments = self.convert_tokens_to_raw_segments(
            tokenizer.get_tokens(message, characters),
        )

        for raw_segment in raw_segments:
            yield self.convert_raw_segment_to_segment(raw_segment, directory=directory)

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

        characters.component_separator = chars[0]
        characters.data_separator = chars[1]
        characters.decimal_point = chars[2]
        characters.escape_character = chars[3]
        characters.reserved_character = chars[4]
        characters.segment_terminator = chars[5]

        return characters

    def convert_tokens_to_raw_segments(
        self, tokens: Iterator[Token]
    ) -> Iterator[Elements]:
        """Convert the tokenized message into an array of segments.

        Args:
            tokens (Iterator[Token]): The tokens that make up the message
            characters (Characters): The control characters to use

        Returns:
            Iterator[Segment]: An iterator of Segment objects
        """

        current_segment: Elements = []
        data_element: list[str] = []
        data_element_value: Element
        in_segment = False
        empty_component_counter = 0

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
                    yield current_segment
                    continue

            # If we're not in a segment, then start a new empty one now
            # and add it to the list. Also create a new empty data element,
            # because if the next token is a DATA_SEPARATOR, at least we have
            # an empty string to save into the segment then.
            else:
                current_segment = []
                # raw_segments.append(current_segment)
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

    def convert_raw_segment_to_segment(
        self,
        raw_segment: Elements,
        version: str = EDI_DEFAULT_VERSION,
        directory: str = EDI_DEFAULT_DIRECTORY,
    ) -> Segment:
        name = raw_segment.pop(0)
        if isinstance(name, list):
            raise EDISyntaxError("Invalid segment name: {name}")

        if name == "UNA":
            # We found another UNA segment.
            # This is not in the specs, so raise an error
            raise EDISyntaxError("There are not multiple UNA segments allowed.")
        if name == "UNB":
            # here we have the chance to determine the syntax/style and version
            # of the EDI file. We have to inform the factory about it.
            # However, if the syntax is set by force (Parser init parameter),
            # then we don't override it here, even if the UNB segment has another
            # value. The user might want to override this manually.

            print(f"Found edifact syntax '{raw_segment[0][0]}' in UNB header", end="")
            if self.syntax_identifier:
                print(", but using override syntax '{self.syntax_identifier}'")
            else:
                print(".")
                self.syntax_identifier = raw_segment[0][0]

            print(
                f"Found edifact version '{int(raw_segment[0][1])}' in UNB header",
                end="",
            )
            if self.version:
                print(f", but using override version '{self.version}'.")

            else:
                self.version = int(raw_segment[0][1])
                print(".")
        return self.factory.create_segment(
            name,
            *raw_segment,
            version=self.version,
            directory=directory,
            syntax_identifier=self.syntax_identifier or EDI_DEFAULT_SYNTAX,
        )
