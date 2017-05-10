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

from pydifact.Token import Token
from pydifact.ControlCharacter import ControlCharacterMixin


class Tokenizer(ControlCharacterMixin):
    """Convert EDI messages into tokens for parsing."""

    def __init__(self):
        super().__init__()

        # The message that we are tokenizing.
        self._message = ""

        # The current character from the message we are dealing with.
        self.char = ""

        # The stored characters for the next token.
        self.string = ""

        # bool $isEscaped If the current character has been esacped.
        self.isEscaped = False

    def getTokens(self, message: str) -> list:
        """Convert the passed message into tokens.
        :param message: The EDI message
        :return: Token[]
        """

        self.message = message
        self.char = None
        self.string = ""
        self.readNextChar()
        tokens = []

        # FIXME: do this more pythonic:
        token = self.getNextToken()
        while token:
            tokens.append(token)
            token = self.getNextToken()

        return tokens

    def readNextChar(self) -> str:
        """Read the next character from the message."""
        self.char = self.getNextChar()

        # If the last character was escaped, this one can't possibly be
        if (self.isEscaped):
            self.isEscaped = False

        # If this is the escape character, then read the next one and
        # flag the next as escaped
        if self.char == self.escapeCharacter:
            self.char = self.getNextChar()
            self.isEscaped = True

    def getNextChar(self) -> str:
        """Get the next character from the message."""

        char = self.message[0:1]
        self.message = self.message[1:]
        return char

    def getNextToken(self) -> Token or None:
        """Get the next token from the message."""

        if self.endOfMessage():
            return

        # If we're not escaping this character then see if it's
        # a control character
        if not self.isEscaped:
            if self.char == self.componentSeparator:
                self.storeCurrentCharAndReadNext()
                return Token(Token.COMPONENT_SEPARATOR,
                             self.extractStoredChars())

            if self.char == self.dataSeparator:
                self.storeCurrentCharAndReadNext()
                return Token(Token.DATA_SEPARATOR, self.extractStoredChars())

            if self.char == self.segmentTerminator:
                self.storeCurrentCharAndReadNext()
                token = Token(Token.TERMINATOR, self.extractStoredChars())

                # Ignore any trailing space after the end of the segment
                while self.char in ["\r", "\n"]:
                    self.readNextChar()

                return token

        while not self.isControlCharacter():
            if self.endOfMessage():
                raise RuntimeError("Unexpected end of EDI message")

            self.storeCurrentCharAndReadNext()

        return Token(Token.CONTENT, self.extractStoredChars())

    def isControlCharacter(self) -> bool:
        """Check if the current character is a control character."""

        if (self.isEscaped):
            return False

        return self.char in [
            self.componentSeparator, self.dataSeparator, self.segmentTerminator
            ]

    def storeCurrentCharAndReadNext(self) -> None:
        """Store the current character and read the
        next one from the message.
        """

        self.string += self.char
        self.readNextChar()

    def extractStoredChars(self) -> str:
        """Get the previously stored characters. """

        string = self.string
        self.string = ""
        return string

    def endOfMessage(self) -> None:
        """Check if we've reached the end of the message"""

        return len(self.char) == 0
