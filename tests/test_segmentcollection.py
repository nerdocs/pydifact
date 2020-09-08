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
import datetime

import pytest

from pydifact.segmentcollection import Interchange, Message, SegmentCollection
from pydifact.segments import Segment
from pydifact.api import EDISyntaxError


def test_from_file():
    with pytest.raises(FileNotFoundError):
        SegmentCollection.from_file("/no/such/file")


def test_create_with_segments():
    collection = SegmentCollection.from_segments([Segment("36CF")])
    assert [Segment("36CF")] == collection.segments


def test_get_segments():
    collection = SegmentCollection.from_segments(
        [Segment("36CF", 1), Segment("CPD"), Segment("36CF", 2)]
    )
    segments = list(collection.get_segments("36CF"))
    assert [Segment("36CF", 1), Segment("36CF", 2)] == segments


def test_get_segments_doesnt_exist():
    collection = SegmentCollection()
    segments = list(collection.get_segments("36CF"))
    assert [] == segments


def test_get_segment():
    collection = SegmentCollection.from_segments(
        [Segment("36CF", 1), Segment("36CF", 2)]
    )
    segment = collection.get_segment("36CF")
    assert Segment("36CF", 1) == segment


def test_str_serialize():
    collection = SegmentCollection.from_segments(
        [Segment("36CF", "1"), Segment("36CF", "2")]
    )
    string = str(collection)
    assert "36CF+1'36CF+2'" == string


def test_get_segment_doesnt_exist():
    collection = SegmentCollection()
    segment = collection.get_segment("36CF")
    assert segment is None


def test_empty_segment():
    m = SegmentCollection()
    m.add_segment(Segment("", []))
    assert m


def test_malformed_tag1():
    with pytest.raises(EDISyntaxError):
        SegmentCollection.from_str("IMD+F++:::This is 'a :malformed string'")


def test_malformed_tag2():
    with pytest.raises(EDISyntaxError):
        SegmentCollection.from_str("IMD+F++:::This is '? :malformed string'")


def test_malformed_tag3():
    with pytest.raises(EDISyntaxError):
        SegmentCollection.from_str("IMD+F++:::This is '?? :malformed string'")


def test_malformed_tag4():
    with pytest.raises(EDISyntaxError):
        SegmentCollection.from_str("IMD+F++:::This is '??:malformed string'")


def test_malformed_tag5():
    with pytest.raises(EDISyntaxError):
        SegmentCollection.from_str("IMD+F++:::This is '-:malformed string'")


def test_empty_interchange():
    i = Interchange(
        sender='1234',
        recipient='3333',
        timestamp=datetime.datetime(2020,1,2,22,12),
        control_reference='42',
        syntax_identifier=('UNOC', 1),
    )

    assert str(i) == (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNZ+0+42'"
    )


def test_empty_interchange_from_str():
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNZ+0+42'"
    )
    assert str(i) == (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNZ+0+42'"
    )


def test_empty_message():
    m = Message(
        reference_number='42z42',
        identifier=('PAORES', 93, 1, 'IA'),
    )

    assert str(m) == (
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+42z42+0'"
    )
