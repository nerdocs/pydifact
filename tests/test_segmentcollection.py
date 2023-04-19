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
from typing import Iterable, List

import pytest

from pydifact import Serializer
from pydifact.segmentcollection import Interchange, Message, RawSegmentCollection
from pydifact.segments import Segment
from pydifact.api import EDISyntaxError


def test_from_file():
    with pytest.raises(FileNotFoundError):
        Interchange.from_file("/no/such/file")


def test_create_with_segments():
    collection = RawSegmentCollection.from_segments([Segment("36CF")])
    assert [Segment("36CF")] == collection.segments


def test_get_segments():
    collection = RawSegmentCollection.from_segments(
        [Segment("36CF", 1), Segment("CPD"), Segment("36CF", 2)]
    )
    segments = list(collection.get_segments("36CF"))
    assert [Segment("36CF", 1), Segment("36CF", 2)] == segments


def test_get_segments_doesnt_exist():
    collection = RawSegmentCollection()
    segments = list(collection.get_segments("36CF"))
    assert [] == segments


def test_get_segments_w_predicate():
    collection = RawSegmentCollection.from_segments(
        [
            Segment("A", "1", "a"),
            Segment("A", "2", "b"),
            Segment("A", "1", "c"),
        ]
    )
    segments = collection.get_segments("A", lambda x: x[0] == "1")
    assert [
        Segment("A", "1", "a"),
        Segment("A", "1", "c"),
    ] == list(segments)


def test_get_segment():
    collection = RawSegmentCollection.from_segments(
        [Segment("36CF", 1), Segment("36CF", 2)]
    )
    segment = collection.get_segment("36CF")
    assert Segment("36CF", 1) == segment


def test_get_segment_w_predicate():
    collection = RawSegmentCollection.from_segments(
        [Segment("36CF", "1"), Segment("36CF", "2")]
    )
    segment = collection.get_segment("36CF", lambda x: x[0] == "2")
    assert segment == Segment("36CF", "2")


def test_split_by():
    def _serialize(collections: Iterable[RawSegmentCollection]) -> List[List[str]]:
        lst = []
        global_lst = []
        for collection in collections:
            if lst:
                global_lst.append(lst)
                lst = []
            for segment in collection.segments:
                lst.append(segment.tag)
        if lst:
            global_lst.append(lst)
        return global_lst

    assert _serialize(RawSegmentCollection.from_segments([]).split_by("A")) == []
    collection = RawSegmentCollection.from_segments(
        Segment(i) for i in ["A", "B", "A", "A", "B", "D"]
    )
    assert _serialize(collection.split_by("Z")) == []
    assert _serialize(collection.split_by("A")) == [["A", "B"], ["A"], ["A", "B", "D"]]
    assert _serialize(collection.split_by("A")) == [["A", "B"], ["A"], ["A", "B", "D"]]


def test_str_serialize():
    collection = RawSegmentCollection.from_segments(
        [Segment("36CF", "1"), Segment("36CF", "2")]
    )
    string = str(collection)
    assert "36CF+1'36CF+2'" == string


def test_get_segment_doesnt_exist():
    collection = RawSegmentCollection()
    segment = collection.get_segment("36CF")
    assert segment is None


def test_empty_segment():
    m = RawSegmentCollection()
    m.add_segment(Segment("", []))
    assert m


def test_malformed_tag1():
    with pytest.raises(EDISyntaxError):
        RawSegmentCollection.from_str("IMD+F++:::This is 'a :malformed string'")


def test_malformed_tag2():
    with pytest.raises(EDISyntaxError):
        RawSegmentCollection.from_str("IMD+F++:::This is '? :malformed string'")


def test_malformed_tag3():
    with pytest.raises(EDISyntaxError):
        RawSegmentCollection.from_str("IMD+F++:::This is '?? :malformed string'")


def test_malformed_tag4():
    with pytest.raises(EDISyntaxError):
        RawSegmentCollection.from_str("IMD+F++:::This is '??:malformed string'")


def test_malformed_tag5():
    with pytest.raises(EDISyntaxError):
        RawSegmentCollection.from_str("IMD+F++:::This is '-:malformed string'")


@pytest.fixture
def interchange():
    return Interchange(
        sender="1234",
        recipient="3333",
        timestamp=datetime.datetime(2020, 1, 2, 22, 12),
        control_reference="42",
        syntax_identifier=("UNOC", 1),
    )


@pytest.fixture
def message():
    return Message(
        reference_number="42z42",
        identifier=("PAORES", 93, 1, "IA"),
    )


def test_empty_interchange(interchange):
    assert str(interchange) == ("UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")


def test_empty_interchange_w_extra_header(interchange):
    i = Interchange(
        sender="1234",
        recipient="3333",
        timestamp=datetime.datetime(2020, 1, 2, 22, 12),
        control_reference="42",
        syntax_identifier=("UNOC", 1),
        extra_header_elements=[["66", "2"], "ZZ"],
    )

    assert str(i) == ("UNB+UNOC:1+1234+3333+200102:2212+42+66:2+ZZ'" "UNZ+0+42'")


def test_empty_interchange_from_str():
    i = Interchange.from_str("UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")
    assert str(i) == ("UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")


def test_empty_interchange_w_una():
    i = Interchange.from_segments(
        [
            Segment("UNA", ":+,? '"),
            Segment("UNB", ["UNOC", "1"], "1234", "3333", ["200102", "2212"], "42"),
            Segment("UNZ", "0", "42"),
        ]
    )
    assert str(i) == ("UNA:+,? '" "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")


def test_interchange_messages(interchange, message):
    assert len(list(interchange.get_messages())) == 0

    interchange.add_message(message)

    assert len(list(interchange.get_messages())) == 1

    assert str(interchange) == (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )


def test_interchange_from_str_multi_messages():
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNH+43z43+PAORES:93:1:IA'"
        "UNT+2+43z43'"
        "UNZ+2+42'"
    )

    assert len(list(i.get_messages()))


def test_interchange_messages_from_str():
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )
    assert str(i) == (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )


def test_interchange_with_una():
    i = Interchange.from_str(
        "UNA:+,? '"
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )
    assert i.has_una_segment


def test_interchange_with_custom_character():
    i = Interchange.from_str(
        "UNA:+.? '"
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )
    assert i.characters.decimal_point == "."


def test_faulty_interchange__UNH_not_closed():
    """creates a message with an opening UNH message, without closing UNT"""
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNH+42z42+PAORES:93:1:IA'" "UNZ+2+42'"
    )

    with pytest.raises(EDISyntaxError):
        list(i.get_messages())


def test_faulty_interchange__nested_UNH_not_closed():
    """creates a message with 2 nested UNH, one of them not closed"""
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNZ+2+42'"
    )

    with pytest.raises(EDISyntaxError):
        list(i.get_messages())


def test_faulty_interchange__UNT_without_UNH():
    """creates a message with an cloding UNT, without UNH"""
    i = Interchange.from_str(
        "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNT+2+42z42'" "UNZ+2+42'"
    )

    with pytest.raises(EDISyntaxError):
        list(i.get_messages())


def test_empty_message(message):
    assert str(message) == ("UNH+42z42+PAORES:93:1:IA'" "UNT+2+42z42'")


def test_add_another_footer_element(message):
    """make sure that adding another UNZ footer is ignored."""
    assert message.add_segment(Segment("UNZ", "1", "234z45")) == message


def test_counting_of_messages(interchange, message):
    edi_str = (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNH+42z43+PAORES:93:1:IA'"
        "UNT+2+42z43'"
        "UNZ+2+42'"
    )
    i = Interchange.from_str(edi_str)
    assert i.serialize() == edi_str
