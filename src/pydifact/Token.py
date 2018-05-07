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
from enum import Enum


class Token:
    """Represents a block of characters in the message.

    This could be content, a data separator (usually +),
    a component data separator (usually :), or a segment terminator (usually ').
    """
    class Type(Enum):
        CTRL_CHARS = 10                # ASCII string holding the control chars
        CONTENT = 11
        COMPONENT_SEPARATOR = 12    # default :
        DATA_SEPARATOR = 13         # default +
        TERMINATOR = 14             # default '

    def __init__(self, token_type: Type, value: str):
        """Creates a Token with a type and a value"""
        assert type(token_type) == Token.Type

        self.type = token_type
        self.value = value

    def __str__(self) -> str:
        return "'{}' ({})".format(self.value, self.type.name)

    def __eq__(self, other) -> bool:
        return self.type == other.type and self.value == other.value
