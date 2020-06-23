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
from pydifact.segmentcollection import SegmentCollection


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    unb_segment = "UNB+UNOA:4+APIS*ABE+USADHS+070429:0900+000000001++USADHS'"
    cc = Characters()
    setup.cc = cc.with_control_character("decimal_point", ".")
    setup.collection = SegmentCollection.from_str(unb_segment)
    return setup

class TestUNBSegment():
    def test_una_decimal_point(self, setup):
        assert setup.cc.decimal_point == "."

    def test_unb_segement(self, setup):
        segment = setup.collection.segments[0]
        assert segment.tag == 'UNB'
        assert segment.elements[0][0] == 'UNOA'
        assert segment.elements[0][1] == '4'
        assert segment.elements[1] == 'APIS*ABE'
        assert segment.elements[2] == 'USADHS'
        assert segment.elements[3][0] == '070429'
        assert segment.elements[3][1] == '0900'
        assert segment.elements[4] == '000000001'
        assert segment.elements[5] == ''
        assert segment.elements[6] == 'USADHS'
