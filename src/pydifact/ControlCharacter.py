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


class ControlCharacterMixin:

    def __init__(self):
        # The control character used to separate components.
        self._component_separator = ':'

        # The control character used to separate data elements.
        self._data_separator = '+'

        # The control character used as a decimal point.
        self._decimal_point = ','

        # The control character used as an escape character.
        self._escape_character = '?'

        # Reserved for future use
        self._reserved_character = ' '

        # The control character used as an segment terminator.
        self._segment_terminator = "'"

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
        if not hasattr(self, '_' + cc_type):
            raise AttributeError(
                "{} doesn't have an attribute with the name '_{}'".format(
                    self, cc_type)
            )
        setattr(self, '_' + cc_type, char)
        return self

    def set_component_separator(self, char: str):
        """Set the control character used to separate components.
        :param char: The character to use
        """
        return self.set_control_character("component_separator", char)

    def set_data_separator(self, char: str):
        """Set the control character used to separate data elements.
        :param char: The character to use
        """
        return self.set_control_character("data_separator", char)

    def set_decimal_point(self, char: str):
        """Set the control character used as a decimal point.
        :param char: The character to use
        """
        return self.set_control_character("decimal_point", char)

    def set_escape_character(self, char: str):
        """Set the control character used as an escape character.
        :param char: The character to use
        """
        return self.set_control_character("escape_character", char)

    def set_reserved_character(self, char: str = " "):
        """
        Set the control character used as an segment terminator.
        :param char: The character to use
        """
        return self.set_control_character("reserved_character", char)

    def set_segment_terminator(self, char: str):
        """
        Set the control character used as an segment terminator.
        :param char: The character to use
        """
        return self.set_control_character("segment_terminator", char)
