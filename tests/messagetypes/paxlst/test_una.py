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
import pytest
from pydifact.control import Characters


def setup_module(module):
    global una_segment
    global cc
    una_segment = "UNA:+.? '"
    cc = Characters.from_str(una_segment)


class TestUNASegment():

    def test_una_sgement(self):
        assert cc.component_separator == ":"
        assert cc.data_separator == "+"
        assert cc.decimal_point == "."
        assert cc.escape_character == "?"
        assert cc.reserved_character == " "
        assert cc.segment_terminator == "'"
