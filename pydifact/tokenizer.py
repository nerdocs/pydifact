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

from pydifact.token import Token
from pydifact.control.characters import Characters
from typing import Union, List, Optional


class Tokenizer:
    """Convert EDI messages into tokens for parsing."""

    def __init__(self):
        super().__init__()

        # The message that we are tokenizing.
        self._message = []

        self._current_chars = []

        # The current character from the message we are dealing with.
        self._char = ""

        # The stored characters for the next token.
        self._string = ""

        # bool isEscaped If the current character has been escaped.
        self.isEscaped = False

        # The control characters for the message
        self.characters = None

        self.token_selector = {}

        self._message_index = 0

    def get_tokens(self, message: str, characters: Characters = None) -> List[Token]:
        """Convert the passed message into tokens.
        :param characters: the Control Characters to use for tokenizing. If omitted, use a default set.
        :param message: The EDI message
        :return: Token[]
        """

        self.characters = characters or Characters()
        self._char = None
        self._message = iter(message)
        self._message_index = 0
        self.read_next_char()

        self.token_selector = {
            self.characters.component_separator: Token.Type.COMPONENT_SEPARATOR,
            self.characters.data_separator: Token.Type.DATA_SEPARATOR,
            self.characters.segment_terminator: Token.Type.TERMINATOR,
        }

        while not self.end_of_message():
            yield self.get_next_token()

    def read_next_char(self) -> None:
        """Read the next character from the message.

        If the character is an escape character, set the isEscaped flag to
        True, get the one after it and store that character in the internal storage."""

        # first, get the next char.
        self._char = self.get_next_char()

        # If the last character was escaped, this one can't possibly be an escaped one.
        if self.isEscaped:
            self.isEscaped = False

        # If this is the escape character, then read the next one, store it and
        # flag it as escaped
        if self._char == self.characters.escape_character:
            self.isEscaped = True
            self._char = self.get_next_char()

    def get_next_char(self) -> Union[str, None]:
        """Get the next character from the message."""
        try:
            return next(self._message)
        except StopIteration:
            return

    def get_next_token(self) -> Optional[Token]:
        """Get the next token from the message."""

        # If we're not escaping this character then see if it's
        # a control character

        token_type = not self.isEscaped and self.token_selector.get(self._char)
        if token_type:
            self.store_current_char_and_read_next()
            token = Token(token_type, self.extract_stored_chars())
            if token_type == Token.Type.TERMINATOR:
                while self._char in self.characters.line_terminators:
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

        return self._char in self.token_selector

    def store_current_char_and_read_next(self) -> None:
        """Store the current character and read the
        next one from the message."""

        self._current_chars.append(self._char)
        self.read_next_char()

    def extract_stored_chars(self) -> str:
        """Return the previously stored characters and empty the store."""

        chars = self._current_chars
        self._current_chars = []
        return "".join(chars)

    def end_of_message(self) -> bool:
        """Check if we've reached the end of the message"""
        return self._char is None

    def __str__(self):
        return "".join(self._current_chars)
