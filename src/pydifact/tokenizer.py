#    pydifact - a python edifact library
#    Copyright (C) 2017-2018  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from pydifact.token import Token
from pydifact.control.characters import Characters
from typing import Union


class Tokenizer:
    """Convert EDI messages into tokens for parsing."""

    def __init__(self):
        super().__init__()

        # The message that we are tokenizing.
        self._message = []

        # The current character from the message we are dealing with.
        self._char = ""

        # The stored characters for the next token.
        self._string = ""

        # bool isEscaped If the current character has been escaped.
        self.isEscaped = False

        # The control characters for the message
        self.characters = None

    def get_tokens(self, message: str, characters: Characters) -> list:
        """Convert the passed message into tokens.
        :param characters:
        :param message: The EDI message
        :return: Token[]
        """

        self.characters = characters
        self._char = None
        self._string = ''
        self._message = iter(message)
        self._message_index = 0
        self.read_next_char()
        tokens = []


        # FIXME: do this more pythonic:
        token = self.get_next_token()
        while token:
            tokens.append(token)
            token = self.get_next_token()

        return tokens

    def read_next_char(self) -> None:
        """Read the next character from the message.

        If the character is an escape character, set the isEscaped flag to
        True, get the one after it and return that."""

        self._char = self.get_next_char()

        # If the last character was escaped, this one can't possibly be
        if self.isEscaped:
            self.isEscaped = False

        # If this is the escape character, then read the next one and
        # flag the next as escaped
        if self._char == self.characters.escape_character:
            self._char = self.get_next_char()
            self.isEscaped = True

    def get_next_char(self) -> Union[str, None]:
        """Get the next character from the message."""
        try:
            return next(self._message)
        except StopIteration:
            return

    def get_next_token(self) -> Token or None:
        """Get the next token from the message."""

        if self.end_of_message():
            return None

        # If we're not escaping this character then see if it's
        # a control character
        if not self.isEscaped:
            if self._char == self.characters.component_separator:
                self.store_current_char_and_read_next()
                return Token(Token.Type.COMPONENT_SEPARATOR,
                             self.extract_stored_chars())

            if self._char == self.characters.data_separator:
                self.store_current_char_and_read_next()
                return Token(Token.Type.DATA_SEPARATOR, self.extract_stored_chars())

            if self._char == self.characters.segment_terminator:
                self.store_current_char_and_read_next()
                token = Token(Token.Type.TERMINATOR, self.extract_stored_chars())

                # Ignore any trailing space after the end of the segment
                while self._char in ["\r", "\n"]:
                    self.read_next_char()

                return token

        while not self.is_control_character():
            if self.end_of_message():
                raise RuntimeError("Unexpected end of EDI message")

            self.store_current_char_and_read_next()

        return Token(Token.Type.CONTENT, self.extract_stored_chars())

    def is_control_character(self) -> bool:
        """Check if the current character is a control character."""

        if self.isEscaped:
            return False

        return self._char in [
            self.characters.component_separator,
            self.characters.data_separator,
            self.characters.segment_terminator
            ]

    def store_current_char_and_read_next(self) -> None:
        """Store the current character and read the
        next one from the message."""

        self._string += self._char
        self.read_next_char()

    def extract_stored_chars(self) -> str:
        """Get the previously stored characters and empty the store."""

        string = self._string
        self._string = ""
        return string

    def end_of_message(self) -> bool:
        """Check if we've reached the end of the message"""
        return self._char is None
