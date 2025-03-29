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

from enum import Enum


class TokenType(Enum):
    CTRL_CHARS = 10  # ASCII string holding the control chars
    CONTENT = 11
    COMPONENT_SEPARATOR = 12  # default :
    DATA_SEPARATOR = 13  # default +
    TERMINATOR = 14  # default '


class Token:
    """Represents a block of characters in the message.

    This could be content, a data separator (usually +),
    a component data separator (usually :), or a segment terminator (usually ').
    """

    def __init__(self, token_type: TokenType, value: str):
        """Creates a Token with a type and a value"""
        if not isinstance(token_type, TokenType):
            raise TypeError(f"Invalid token type: {token_type}")

        self.type = token_type
        self.value = value

    def __str__(self) -> str:
        return f"{self.type.name} Token: '{self.value}'"

    def __repr__(self) -> str:
        return f"<{self.type.name} Token object '{self.value}' at {hex(id(self))}>"

    def __eq__(self, other) -> bool:
        return self.type == other.type and self.value == other.value
