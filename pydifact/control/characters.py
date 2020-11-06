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


from copy import copy


class Characters:
    """A set of control characters to use."""

    def __init__(self):
        # The control character used to separate components.
        self.component_separator = ":"

        # The control character used to separate data elements.
        self.data_separator = "+"

        # The control character used as a decimal point.
        self.decimal_point = ","

        # The control character used as an escape character.
        self.escape_character = "?"

        # Reserved for future use
        self.reserved_character = " "

        # The control character used as an segment terminator.
        self.segment_terminator = "'"

        self.line_terminators = [" ", "\r", "\n"]

    @classmethod
    def from_str(cls, string: str) -> "Characters":
        """Returns a new instance with control characters set to given string.
        :param string: The string to set the control characters to
        """
        if string[0:3] == "UNA":
            string = string[3:9]
        assert len(string) >= 6

        characters = cls()
        characters.component_separator = string[0]
        characters.data_separator = string[1]
        characters.decimal_point = string[2]
        characters.escape_character = string[3]
        characters.reserved_character = string[4]
        characters.segment_terminator = string[5]
        return characters

    def with_control_character(self, cc_type: str, char: str):
        """Set a control character.

        :param cc_type: The type of control character to set,
            as one of the following attribute strings:
            componentSeparator, dataSeparator, decimalPoint,
            escapeCharacter, segmentTerminator
        :param char: The character to set it to
        :return: clone of self
        """
        if len(char) != 1:
            raise ValueError("control characters must only be a single character")

        # set the attribute dynamically.
        if not hasattr(self, cc_type):
            raise AttributeError(
                "{} doesn't have an attribute with the name '{}'".format(self, cc_type)
            )

        other = copy(self)
        setattr(other, cc_type, char)

        # return clone
        return other

    @property
    def service_string_advice(self) -> str:
        return "UNA" + str(self)

    @property
    def escaped_syntax_dic(self):
        return {
            self.escape_character: self.escape_character + self.escape_character,
            self.component_separator: self.escape_character + self.component_separator,
            self.data_separator: self.escape_character + self.data_separator,
            self.segment_terminator: self.escape_character + self.segment_terminator,
        }

    def __str__(self) -> str:
        return str(
            self.component_separator
            + self.data_separator
            + self.decimal_point
            + self.escape_character
            + self.reserved_character
            + self.segment_terminator
        )

    def __repr__(self):
        return "'{}'".format(self.__str__())

    def __eq__(self, other):
        if type(other) == str:
            other = Characters.from_str(other)
        return (
            (self.component_separator == other.component_separator)
            and (self.data_separator == other.data_separator)
            and (self.decimal_point == other.decimal_point)
            and (self.escape_character == other.escape_character)
            and (self.reserved_character == other.reserved_character)
            and (self.segment_terminator == other.segment_terminator)
        )
