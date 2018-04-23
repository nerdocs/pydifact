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
        # The control character used to separate components.
        self.componentSeparator = ':'

        # The control character used to separate data elements.
        self.dataSeparator = '+'

        # The control character used as a decimal point.
        self.decimalPoint = ','

        # The control character used as an escape character.
        self.escapeCharacter = '?'

        # Reserved for future use
        self.reservedCharacter = ' '

        # The control character used as an segment terminator.
        self.segmentTerminator = "'"

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
        """Set the control character used to separate components.
        :param char: The character to use
        """
        return self.set_control_character("componentSeparator", char)

    def set_data_separator(self, char: str):
        """Set the control character used to separate data elements.
        :param char: The character to use
        """
        return self.set_control_character("dataSeparator", char)

    def set_decimal_point(self, char: str):
        """Set the control character used as a decimal point.
        :param char: The character to use
        """
        return self.set_control_character("decimalPoint", char)

    def set_escape_character(self, char: str):
        """Set the control character used as an escape character.
        :param char: The character to use
        """
        return self.set_control_character("escapeCharacter", char)

    def set_segment_terminator(self, char: str):
        """
        Set the control character used as an segment terminator.
        :param char: The character to use
        """
        return self.set_control_character("segmentTerminator", char)
