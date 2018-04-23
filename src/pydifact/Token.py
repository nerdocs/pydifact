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


class Token:
    """Represents a block of characters in the message.

    This could be content, a component separator (usually +),
    a data separator (usually :), or a segment terminator (usually ').
    """
    CONTENT = 11
    COMPONENT_SEPARATOR = 12
    DATA_SEPARATOR = 13
    TERMINATOR = 14

    def __init__(self, token_type, value):
        """Creates a Token with a type and a value"""

        self.type = token_type
        self.value = value

    def __str__(self) -> str:
        return "{} ({})".format(self.value, self.type)

    def __eq__(self, other) -> bool:
        return self.type == other.type and self.value == other.value
