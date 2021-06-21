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
import copy
import datetime
import pytest

from pydifact.segmentcollection import RawSegmentCollection, Interchange
from pydifact.segments import Segment
from pydifact.serializer import Serializer


@pytest.fixture
def serializer():
    return Serializer()


@pytest.fixture
def interchange():
    return Interchange(
        sender="1234",
        recipient="3333",
        timestamp=datetime.datetime(2020, 1, 2, 22, 12),
        control_reference="42",
        syntax_identifier=("UNOC", 1),
    )


def assert_segments(serializer, expected: str, segments: list):
    """Helper function add default UNA header and terminator, and compare string to segment"""
    expected = "UNA:+,? '" + expected + "'"
    collection = serializer.serialize(segments, with_una_header=True)
    assert expected == collection


def test_una_integrity1(interchange):
    initstring = ":+,? '"
    interchange.add_segment(Segment("UNA", initstring))
    assert interchange.serialize().startswith("UNA" + initstring)


def test_UNA_integrity2(interchange):
    initstring = ":+.? '"
    interchange.add_segment(Segment("UNA", initstring))
    assert interchange.serialize().startswith("UNA" + initstring)


def test_empty_segment_list():
    m = RawSegmentCollection()
    assert m.serialize() == ""


def test_basic1(serializer):
    assert_segments(serializer, "RFF+PD:50515", [Segment("RFF", ["PD", "50515"])])


def test_basic2(serializer):
    assert_segments(serializer, "RFF+PD+50515", [Segment("RFF", "PD", "50515")])


def test_with_una_in_segments(serializer):
    assert_segments(
        serializer,
        "RFF+PD+45761",
        [Segment("UNA", ":+,? '"), Segment("RFF", "PD", "45761")],
    )


def test_escape_character(serializer):
    assert_segments(
        serializer,
        "ERC+10:The message does not make sense??",
        [Segment("ERC", ["10", "The message does not make sense?"])],
    )


def test_escape_component_separator(serializer):
    assert_segments(
        serializer, "ERC+10:Name?: Craig", [Segment("ERC", ["10", "Name: Craig"])]
    )


def test_escape_data_separator(serializer):
    assert_segments(
        serializer, "DTM+735:?+0000:406", [Segment("DTM", ["735", "+0000", "406"])]
    )


def test_escape_decimal_point(serializer):
    assert_segments(serializer, "QTY+136:12,235", [Segment("QTY", ["136", "12,235"])])


def test_escape_segment_terminator(serializer):
    assert_segments(serializer, "ERC+10:Craig?'s", [Segment("ERC", ["10", "Craig's"])])


def test_escape_sequence(serializer):
    assert_segments(
        serializer,
        "ERC+10:?:?+???' - ?:?+???' - ?:?+???'",
        [Segment("ERC", ["10", ":+?' - :+?' - :+?'"])],
    )


def test_no_mutation(serializer):
    segments1 = [Segment("ERC", [":+?'"])]
    segments2 = copy.deepcopy(segments1)
    serializer.serialize(segments1, with_una_header=True)
    assert segments1 == segments2
