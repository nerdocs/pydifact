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

    CONTENT               =   11
    COMPONENT_SEPARATOR   =   12
    DATA_SEPARATOR        =   13
    TERMINATOR            =   14
    
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value
    
    def __str__(self):
        return "{} ({})".format(self.value, self.type)
    
    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
