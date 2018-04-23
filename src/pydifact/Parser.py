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
from pydifact.Segment import Segment


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
        # continues with cyryllic or UTF-16.
        if not message[:3] == "UNA":
            return None

        # Get the character definitions
        chars = message[3:9]

        tokenizer.setComponentSeparator(chars[0])
        tokenizer.setDataSeparator(chars[1])
        tokenizer.setDecimalPoint(chars[2])
        tokenizer.setEscapeCharacter(chars[3])
        tokenizer.setSegmentTerminator(chars[5])

        # Remove the UNA segment from the original message and
        # return this new string
        return message[9:].lstrip() + "\r\n"

    @staticmethod
    def convert_tokens_to_segments(tokens: list):
        """Convert the tokenized message into an array of segments.
        :param tokens: The tokens that make up the message
        :type tokens: list of Token
        :rtype list of Segment
        """

        segments = []
        data_element = None
        is_composite = False
        in_segment = False

        for token in tokens:

            # If we're in the middle of a segment,
            # check if we've reached the end
            if in_segment:
                if token.type == Token.TERMINATOR:
                    in_segment = False
                    continue

            # If we're not in a segment, then start a new empty one now
            # and add it to the list. Also create a new empty data element,
            # because if the next token is a DATA_SEPARATOR, at least we have
            # an empty string to save into the segment then.
            else:
                in_segment = True
                is_composite = False
                # create a new, empty segment, and append it to
                # the list of segments
                current_segment = []
                segments.append(current_segment)

            # then proceed with ex exploration of the token

            # Whenever we reach a data separator (+), we add the currently
            # collected data element to the current segment (whatever it is,
            # a string or list, and reset the data_element to ""
            if token.type == Token.DATA_SEPARATOR:
                current_segment.append(data_element)
                is_composite = False
                data_element = ""
                continue

            # Whenever we reach a component data separator (:), we know that
            # the whole data element is a composite, so make a list out of
            # the data_element if it isn't already one.
            if token.type == Token.COMPONENT_SEPARATOR:
                is_composite = True
                if not type(data_element) == list:
                    data_element = [data_element]
                continue

            # If this is a composite element, append the string to it
            if is_composite:
                data_element.append(token.value)
                continue
            else:
                # if not a composite (as far as we know yet), add as string
                data_element = token.value
                continue

        for segment in segments:
            name = segment.pop(0)
            yield Segment(name, *segment)
