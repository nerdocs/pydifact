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

from pydifact.segmentcollection import SegmentCollection
from pydifact.segments import Segment


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
    with pytest.raises(ValueError):
        m.add_segment(Segment("", []))
