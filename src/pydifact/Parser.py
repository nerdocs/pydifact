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
from pydifact.Tokenizer import Tokenizer
from pydifact.Token import Token
from pydifact.Segments import Segment


class Parser:
    """Parse EDI messages into an array of segments."""

    def parse(self, message: str) -> list:
        """Parse the message into an array of segments.
        :param message: The EDI message
        :rtype: list
        """

        tokenizer = Tokenizer()
        message = self.setup_special_characters(message, tokenizer)
        tokens = tokenizer.get_tokens(message)
        segments = self.convert_tokens_to_segments(tokens)
        return segments

    @staticmethod
    def setup_special_characters(message: str,
                                 tokenizer: Tokenizer) -> str or None:
        """Read (and remove) the UNA segment from the passed string.

        :param message: The EDI message to extract the UNA from
        :param tokenizer:
        :type tokenizer: Tokenizer
        :rtype: str or None
        :return: the message string without the UNA header, or None
            if the message does not start with "UNA"
        """

        # The UNA segment (if exists) and the UNB segment must always be ASCII, even if after the BGM the files
        # continues with cyrillic or UTF-16.
        if not message[:3] == "UNA":
            return None

        # Get the character definitions
        chars = message[3:9]

        tokenizer.set_component_separator(chars[0])
        tokenizer.set_data_separator(chars[1])
        tokenizer.set_decimal_point(chars[2])
        tokenizer.set_escape_character(chars[3])
        tokenizer.set_reserved_character(chars[4])
        tokenizer.set_segment_terminator(chars[5])

        # Remove the UNA segment from the original message and
        # return this new string
        return message[9:].lstrip()

    @staticmethod
    def convert_tokens_to_segments(tokens: list):
        """Convert the tokenized message into an array of segments.
        :param tokens: The tokens that make up the message
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
                    elif len(data_element) == 1:
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
                empty_component_counter = -1
                continue

            # Whenever we reach a component data separator (:), we know that
            # the whole data element is a composite, so increment the counter
            # this is especially needed when more than one component data
            # separators are in a row "23:::56"
            if token.type == Token.Type.COMPONENT_SEPARATOR:
                empty_component_counter += 1
                continue

            # when we reach here, the token value is "content"

            # backfill empty strings for skipped component data (:::)
            for i in range(0, empty_component_counter):
                data_element.append("")

            data_element.append(token.value)
            empty_component_counter = -1
            continue

#        for segment in segments:
#            name = segment.pop(0)
#            yield Segment(name, *segment)

        segment_list = []
        for segment in segments:
            name = segment.pop(0)
            segment_list.append(Segment(name, *segment))

        return segment_list
