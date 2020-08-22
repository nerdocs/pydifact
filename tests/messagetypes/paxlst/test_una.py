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


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    una_segment = "UNA:+.? '"
    setup.cc = Characters.from_str(una_segment)
    return setup


def test_una_segment(setup):
    assert setup.cc.component_separator == ":"
    assert setup.cc.data_separator == "+"
    assert setup.cc.decimal_point == "."
    assert setup.cc.escape_character == "?"
    assert setup.cc.reserved_character == " "
    assert setup.cc.segment_terminator == "'"
