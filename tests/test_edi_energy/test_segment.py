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

from edi_energy.energy_segments import BGM, UNH, EDISegment as Segment
from edi_energy.energy_segments import choose_segment_from_catalog
from edi_energy.energy_collections import EnergySegmentsContainer


elements = ["field1", ["field2", "extra"], "stuff"]


def test_get_segment_code():
    segment = Segment("OMD")
    assert segment.tag == "OMD"


def test_all_elements():
    segment = Segment("OMD", *elements)
    assert segment.elements == elements


def test_get_single_element():
    segment = Segment("OMD", *elements)
    assert segment.elements[0] == "field1"


def test_get_list_element():
    segment = Segment("OMD", *elements)
    assert segment.elements[1] == ["field2", "extra"]


def test_get_non_existing_element():
    segment = Segment("OMD", *elements)
    with pytest.raises(IndexError):
        segment.elements[7]


@pytest.mark.parametrize(
    "seg_str,output",
    [
        ("UNH+1+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+1:C'", "2.3c"),
        ("UNH+2+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+2'", "2.3c"),
        ("UNH+3+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+3:F'", "2.3c"),
        ("UNH+4+MSCONS:D:04B:UN:2.3c'", "2.3c"),
    ],
)
def test_EDIsegment_from_str(seg_str, output):
    seg = Segment.from_str(seg_str)
    assert isinstance(seg, Segment)
    # ensure segment has at least elements
    assert len(seg.elements) > 0


@pytest.mark.parametrize(
    "seg_str,output",
    [
        ("UNH+1+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+1:C'", "2.3c"),
        ("UNH+2+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+2'", "2.3c"),
        ("UNH+3+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+3:F'", "2.3c"),
        ("UNH+4+MSCONS:D:04B:UN:2.3c'", "2.3c"),
        ("UNH+1+ORDRSP:D:07A:UN:DVGW17'", "DVGW17"),
        ("UNH+438978899+ORDRSP:D:07A:UN:DVGW18'", "DVGW18"),
    ],
)
def test_UNH(seg_str, output):
    seg = Segment.from_str(seg_str)
    assert UNH(seg).usage_code_organisation == output


@pytest.mark.parametrize(
    "seg_str,out",
    [
        ("UNH+1+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+1:C'", False),
        ("UNH+2+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+2'", False),
        ("UNH+3+MSCONS:D:04B:UN:2.3c+UNB_DE0020_nr_1+3:F'", False),
        ("UNH+4+MSCONS:D:04B:UN:2.3c'", False),
        ("UNH+1+ORDRSP:D:07A:UN:DVGW17'", True),
        ("UNH+438978899+ORDRSP:D:07A:UN:DVGW18'", True),
    ],
)
def test_UNH(seg_str, out):
    seg = Segment.from_str(seg_str)
    assert UNH(seg).is_subformat == out


@pytest.mark.parametrize(
    "seg_str,out",
    [
        ("BGM+Z48+100698719676+9'", False),
        ("BGM+Z24+TEST00000517+9'", False),
        ("BGM+7+502887849FB14868870CD84693576199+1'", False),
        ("BGM+X4G::332+ALOCAT438978899'", False),
        ("BGM+14G::332+IMBNOT436521948'", True),
        ("BGM+Z36+041128914202'", True),
    ],
)
def test_UNH(seg_str, out):
    seg = Segment.from_str(seg_str)
    assert BGM(seg)


@pytest.mark.parametrize(
    "seg_str,format",
    [
        ("UNH+100698719676+MSCONS:D:04B:UN:2.3c'BGM+Z48+100698719676+9'", "MSCONS"),
        ("UNH+TEST00000517001+MSCONS:D:04B:UN:2.3c'BGM+Z24+TEST00000517+9'", "MSCONS"),
        (
            "UNH+1+MSCONS:D:04B:UN:2.3c'BGM+7+502887849FB14868870CD84693576199+1'",
            "MSCONS",
        ),
        (
            "UNH+438978899+ORDRSP:D:07A:UN:DVGW18'BGM+X4G::332+ALOCAT438978899'",
            "ORDRSP",
        ),
        (
            "UNH+436521948+ORDRSP:D:08A:UN:DVGW17'BGM+14G::332+IMBNOT436521948'",
            "ORDRSP",
        ),
        ("UNH+1+UTILMD:D:11A:UN:5.2c'BGM+Z07+EC38480624A-1'", "UTILMD"),
        ("UNH+1+UTILMD:D:11A:UN:5.2c'BGM+Z05+TEST00000560-1'", "UTILMD"),
        ("UNH+US0000003108+UTILTS:D:18A:UN:1.0a'BGM+Z36+US0000003108'", "UTILTS"),
        ("UNH+041128914202+UTILTS:D:18A:UN:1.0a'BGM+Z36+041128914202'", "UTILTS"),
    ],
)
def test_message_type(seg_str, format):
    con = EnergySegmentsContainer.from_str(seg_str)
    unh: UNH = con.get_segment(UNH.tag)
    assert unh.message_type == format


# def test_predicate():

#     elements = ["field1", ["field2", "extra"], "stuff"]
