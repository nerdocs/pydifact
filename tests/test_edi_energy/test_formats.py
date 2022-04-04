import datetime
from typing import Iterable, List

from pydifact.edi_energy.energy_collections import EnergySegmentsContainer
from pydifact.edi_energy.energy_collections import EDIEnergyInterchange as Interchange
from pydifact.edi_energy.energy_collections import EDIEnergyMessage as Message

from pydifact.segments import Segment
from pydifact.api import EDISyntaxError


from pydifact.edi_energy.energy_formats import FORMAT_CATALOG, format_selector

import pytest


class TestEnergySegmentsColl:
    def test_create_with_segments(self):
        collection = EnergySegmentsContainer.from_segments([Segment("36CF")])
        assert [Segment("36CF")] == collection.segments

    def test_get_segments(self):
        collection = EnergySegmentsContainer.from_segments(
            [Segment("36CF", 1), Segment("CPD"), Segment("36CF", 2)]
        )
        segments = list(collection.get_segments("36CF"))
        assert [Segment("36CF", 1), Segment("36CF", 2)] == segments

    def test_get_segments_doesnt_exist(self):
        collection = EnergySegmentsContainer()
        segments = list(collection.get_segments("36CF"))
        assert [] == segments

    def test_get_segments_w_predicate(self):
        collection = EnergySegmentsContainer.from_segments(
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

    def test_get_segment(self):
        collection = EnergySegmentsContainer.from_segments(
            [Segment("36CF", 1), Segment("36CF", 2)]
        )
        segment = collection.get_segment("36CF")
        assert Segment("36CF", 1) == segment


def get_interchange_instance(cls):
    return cls(
        sender="1234",
        recipient="3333",
        timestamp=datetime.datetime(2020, 1, 2, 22, 12),
        control_reference="42",
        syntax_identifier=("UNOC", 1),
    )


def get_message_instance(cls):
    return cls(
        reference_number="42z42",
        identifier=("PAORES", 93, 1, "IA"),
    )


@pytest.mark.parametrize(
    "seg_str,format",
    [
        ("UNH+100698719676+MSCONS:D:04B:UN:2.3c'BGM+Z48+100698719676+9'", "MSCONS"),
        (
            "UNH+438978899+ORDRSP:D:07A:UN:DVGW18'BGM+X4G::332+ALOCAT438978899'",
            "ALOCAT",
        ),
        ("UNH+1+UTILMD:D:11A:UN:5.2c'BGM+Z07+EC38480624A-1'", "UTILMD"),
        (
            "UNH+1+MSCONS:D:04B:UN:2.3c'BGM+7+502887849FB14868870CD84693576199+1'",
            "MSCONS",
        ),
    ],
)
def test_message_creator(seg_str, format):
    con = EnergySegmentsContainer.from_str(seg_str)
    format_selector(con.segments)


class TestBase:
    @pytest.mark.parametrize("cls", FORMAT_CATALOG.values())
    def test_from_file(self, cls: Interchange):
        with pytest.raises(FileNotFoundError):
            cls.from_file("/no/such/file")

    @pytest.mark.parametrize("cls", FORMAT_CATALOG.values())
    def test_empty_interchange(self, cls):
        assert str(get_interchange_instance(cls)) == (
            "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'"
        )

    # def test_empty_interchange_w_extra_header(interchange):
    #     i = Interchange(
    #         sender="1234",
    #         recipient="3333",
    #         timestamp=datetime.datetime(2020, 1, 2, 22, 12),
    #         control_reference="42",
    #         syntax_identifier=("UNOC", 1),
    #         extra_header_elements=[["66", "2"], "ZZ"],
    #     )

    #     assert str(i) == ("UNB+UNOC:1+1234+3333+200102:2212+42+66:2+ZZ'" "UNZ+0+42'")

    # def test_empty_interchange_from_str():
    #     i = Interchange.from_str("UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")
    #     assert str(i) == ("UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'")

    # def test_empty_interchange_w_una():
    #     i = Interchange.from_segments(
    #         [
    #             Segment("UNA", ":+,? '"),
    #             Segment("UNB", ["UNOC", "1"], "1234", "3333", ["200102", "2212"], "42"),
    #             Segment("UNZ", "0", "42"),
    #         ]
    #     )
    #     assert str(i) == (
    #         "UNA:+,? '" "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNZ+0+42'"
    #     )

    # def test_interchange_messages(interchange, message):
    #     assert len(list(interchange.get_messages())) == 0

    #     interchange.add_message(message)

    #     assert len(list(interchange.get_messages())) == 1

    #     assert str(interchange) == (
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNT+2+42z42'"
    #         "UNZ+1+42'"
    #     )

    # def test_interchange_from_str_multi_messages():
    #     i = Interchange.from_str(
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNT+2+42z42'"
    #         "UNH+43z43+PAORES:93:1:IA'"
    #         "UNT+2+43z43'"
    #         "UNZ+2+42'"
    #     )

    #     assert len(list(i.get_messages()))

    # def test_interchange_messages_from_str():
    #     i = Interchange.from_str(
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNT+2+42z42'"
    #         "UNZ+1+42'"
    #     )
    #     assert str(i) == (
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNT+2+42z42'"
    #         "UNZ+1+42'"
    #     )

    # def test_faulty_interchange__UNH_not_closed():
    #     """creates a message with an opening UNH message, without closing UNT"""
    #     i = Interchange.from_str(
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNZ+2+42'"
    #     )

    #     with pytest.raises(EDISyntaxError):
    #         list(i.get_messages())

    # def test_faulty_interchange__nested_UNH_not_closed():
    #     """creates a message with 2 nested UNH, one of them not closed"""
    #     i = Interchange.from_str(
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNZ+2+42'"
    #     )

    #     with pytest.raises(EDISyntaxError):
    #         list(i.get_messages())

    # def test_faulty_interchange__UNT_without_UNH():
    #     """creates a message with an cloding UNT, without UNH"""
    #     i = Interchange.from_str(
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'" "UNT+2+42z42'" "UNZ+2+42'"
    #     )

    #     with pytest.raises(EDISyntaxError):
    #         list(i.get_messages())

    # def test_empty_message(message):
    #     assert str(message) == ("UNH+42z42+PAORES:93:1:IA'" "UNT+2+42z42'")

    # def test_add_another_footer_element(message):
    #     """make sure that adding another UNZ footer is ignored."""
    #     assert message.add_segment(Segment("UNZ", "1", "234z45")) == message

    # def test_counting_of_messages(interchange, message):
    #     edi_str = (
    #         "UNB+UNOC:1+1234+3333+200102:2212+42'"
    #         "UNH+42z42+PAORES:93:1:IA'"
    #         "UNT+2+42z42'"
    #         "UNH+42z43+PAORES:93:1:IA'"
    #         "UNT+2+42z43'"
    #         "UNZ+2+42'"
    #     )
    #     i = Interchange.from_str(edi_str)
    #     assert i.serialize() == edi_str
