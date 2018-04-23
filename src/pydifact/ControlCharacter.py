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


class ControlCharacterMixin:

    def __init__(self):
        # str componentSeparator The control character used to
        # separate components.
        self.componentSeparator = ":"

        # str dataSeparator The control character used to separate
        # data elements.
        self.dataSeparator = "+"

        # str decimalPoint The control character used as a decimal point.
        self.decimalPoint = ","

        # str escapeCharacter The control character used as an
        # escape character.
        self.escapeCharacter = "?"

        # string segmentTerminator The control character used as an segment
        # terminator.
        self.segmentTerminator = "'"

        self.reservedCharacter = ' '

    def set_control_character(self, cc_type: str, char: str):
        """Set a control character.

        :param cc_type: The type of control character to set,
            as one of the following attribute strings:
            componentSeparator, dataSeparator, decimalPoint,
            escapeCharacter, segmentTerminator
        :param char: The character to set it to
        :return: self
        """
        if len(char) != 1:
            raise ValueError(
                "Control characters must only be a single character")

        # set the attribute dynamically.
        setattr(self, cc_type, char)
        return self

    def set_component_separator(self, char: str):
        """
        Set the control character used to separate components.
        :param str char: The character to use
        """
        return self.set_control_character("componentSeparator", char)

    def set_data_separator(self, char: str):
        """
        Set the control character used to separate data elements.
        :param str char: The character to use
        """
        return self.set_control_character("dataSeparator", char)

    def set_decimal_point(self, char: str):
        """
        Set the control character used as a decimal point.
        :param str char: The character to use
        """
        return self.set_control_character("decimalPoint", char)

    def set_escape_character(self, char: str):
        """
        Set the control character used as an escape character.
        :param str char: The character to use
        """
        return self.set_control_character("escapeCharacter", char)

    def set_segment_terminator(self, char: str):
        """
        Set the control character used as an segment terminator.
        :param str char: The character to use
        """
        return self.set_control_character("segmentTerminator", char)
