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

from pydifact import Segment
from pydifact.control import Characters
from pydifact.segmentcollection import RawSegmentCollection
from pydifact.syntax import v4


class Setup:
    pass


@pytest.fixture
def setup():
    setup = Setup()
    unb_segment = "UNB+UNOA:4+APIS*ABE+USADHS+07042029:0900+000000001++USADHS'"
    cc = Characters()
    setup.cc = cc.with_control_character("decimal_point", ".")
    setup.collection = RawSegmentCollection.from_str(unb_segment)
    return setup


def test_una_decimal_point(setup):
    assert setup.cc.decimal_point == "."


def test_unb_segement(setup):
    segment = setup.collection.segments[0]
    assert segment.tag == "UNB"
    assert segment.elements[0][0] == "UNOA"
    assert segment.elements[0][1] == "4"
    assert segment.elements[1] == "APIS*ABE"
    assert segment.elements[2] == "USADHS"
    assert segment.elements[3][0] == "07042029"
    assert segment.elements[3][1] == "0900"
    assert segment.elements[4] == "000000001"
    assert segment.elements[5] == ""
    assert segment.elements[6] == "USADHS"


def test_specialized_segment_compare():
    unb_segment = v4.UNBSegment("foo")
    manual_unb_segment1 = Segment("UNB", "foo")
    manual_unb_segment2 = Segment("UNB", "bar")
    assert unb_segment == manual_unb_segment1
    assert unb_segment != manual_unb_segment2
