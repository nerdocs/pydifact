#    pydifact - a python edifact library
#    Copyright (C) 2017-2024  Christian González
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


def test_with_separator_identity():
    one = Characters()
    other = Characters()
    # a copy of a characters object must be equal, but not the same
    assert one == other, f'Objects differ: "{one}", "{other}"'
    assert one is not other


def test_cc_assigning():
    one = Characters()
    one.component_separator = "x"
    assert one.component_separator == "x"
    assert one == "x+,? '"


def test_wrong_cc_assigning():
    with pytest.raises(ValueError):
        Characters().with_control_character("component_separator", "xd")

    with pytest.raises(AttributeError):
        Characters().with_control_character("notexisting", ":")
