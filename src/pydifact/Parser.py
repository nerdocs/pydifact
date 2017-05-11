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
        self.setupSpecialCharacters(message, tokenizer)
        tokens = tokenizer.getTokens(message)
        segments = self.convertTokensToSegments(tokens)
        return segments

    # FIXME this is differene than the PHP version!
    # returns message, instead of altering the message argument
    def setupSpecialCharacters(self,
                               message: str,
                               tokenizer: Tokenizer) -> str or None:
        """Read (and remove) the UNA segment from the passed string.
        :param message: The EDI message to extract the UNA from
        :param tokenizer:
        :type tokenizer: Tokenizer
        :rtype: str or None
        :return the message string without the UNA header, or None
            if the message does not start with "UNA"
        """

        if not message[0:3] == "UNA":
            return None

        # Get the character definitions
        chars = message[3:9]

        # Remove the UNA segment from the original message
        message = message[9:].lstrip() + "\r\n"

        # TODO - ditch mb_substr here!
        pos = 0
        tokenizer.setComponentSeparator(chars[pos:pos+1])
        pos += 1

        tokenizer.setDataSeparator(chars[pos:pos+1])
        pos += 1

        tokenizer.setDecimalPoint(chars[pos:pos+1])
        pos += 1

        tokenizer.setEscapeCharacter(chars[pos:pos+1])
        pos += 1

        # chars[pos:pos+1]
        pos += 1

        tokenizer.setSegmentTerminator(chars[pos:pos+1])

    def convertTokensToSegments(self, tokens: list):
        """Convert the tokenized message into an array of segments.
        :param tokens: The tokens that make up the message
        :type tokens: list of Token
        :rtype list of Segment
        """

        segments = []
        currentSegment = -1
        inSegment = False
        for token in tokens:

            # If we're in the middle of a segment,
            # check if we've reached the end
            if inSegment:
                if token.type == Token.TERMINATOR:
                    inSegment = False
                    continue

            # If we're not in a segment, then start a new one now
            else:
                inSegment = True
                currentSegment += 1
                segments[currentSegment] = []
                part = 0
                key = 0

            # Whenever we reach a data separator, we increment
            # the part counter to move on to the next part of data,
            # and reset our key counter for the elements within the part.
            if token.type == Token.DATA_SEPARATOR:
                part += 1
                key = 0
                continue

            # Whenever we reach a component separator, we just
            # increment the $key counter for the elements within the
            # current part.
            if token.type == Token.COMPONENT_SEPARATOR:
                key += 1
                continue

            # If this isn't the first part, then backfill any missing parts.
            # This is because empty parts are not represented by a token,
            # so we need to simulate them here.
            if part > 0:
                for i in range(0, part):
                    try:
                        segments[currentSegment][i]
                    except IndexError:
                        segments[currentSegment][i] = ""

            # If this is the first element within the part then just
            # set it as a string.
            if key == 0:
                segments[currentSegment][part] = token.value
                continue

            # For the same as the parts, we need to backfill any empty
            # elements. We also use this code to append the element we are
            # currently processing.
            for i in range(0, key):
                value = token.value if i == key else ""

                # If there is an initial element set as a string, we need
                # to convert it into an array before we append to it
                try:
                    if not type(segments[currentSegment][part]) == list:
                        segments[currentSegment][part] = [
                            segments[currentSegment][part]
                            ]
                except IndexError:
                    pass

                # If this part does not exist, set it now
                try:
                    segments[currentSegment][part][i]
                except IndexError:
                    segments[currentSegment][part][i] = value

        for segment in segments:
            name = segment.pop(0)
            yield Segment(name, *segment)
