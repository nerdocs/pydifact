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
import xml.etree.ElementTree as ET

import pytest

from pydifact import segments
from pydifact.exceptions import (
    MissingImplementationWarning,
    NonConformantEDIWarning,
    ValidationError,
)
from pydifact.parser import Parser
from pydifact.segments import Segment

elements = ["field1", ["field2", "extra"], "stuff"]


def test_get_segment_code_empty():
    # check if pytest output contains warning
    with pytest.warns(NonConformantEDIWarning):
        Segment("OMD")  # noqa


def test_get_segment_code():
    segment = Segment("OMD", "")
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
        segment.elements[7]  # noqa


def test_invalid_segment_tag():
    # Tag must be uppercase
    with pytest.raises(
        ValueError, match="Segment tag must be an uppercase 3-letter string"
    ):
        Segment("omd", "element")

    # Tag must be 3 characters
    with pytest.raises(
        ValueError, match="Segment tag must be an uppercase 3-letter string"
    ):
        Segment("OM", "element")
    with pytest.raises(
        ValueError, match="Segment tag must be an uppercase 3-letter string"
    ):
        Segment("OMDA", "element")

    # Tag must be alphanumeric
    with pytest.raises(
        ValueError, match="Segment tag must be an uppercase 3-letter string"
    ):
        Segment("OM!", "element")

    # Tag must be a string
    with pytest.raises(
        ValueError, match="Segment tag must be an uppercase 3-letter string"
    ):
        Segment(123, "element")


def test_validate_missing_directory_warns_not_raises():
    """Regression: validate() must emit MissingImplementationWarning and not
    raise when segments.xml is absent for the given directory."""
    seg = Segment("BGM", ["380"], "1")
    with pytest.warns(MissingImplementationWarning):
        seg.validate(syntax_version="1", directory="nonexistent_dir")


def test_has_plugin():
    class TestSegment(Segment):
        tag = "TES"

        __omitted__ = False

        def validate(self, *args, **kwargs):
            pass

    assert Segment.plugins[("TES", "4")] is TestSegment


def test_factory_normalises_version_type():
    """The syntax version is compared as str, an int works the same."""
    from pydifact.segments import SegmentFactory
    from pydifact.syntax import v4

    elements = (["UNOC", "4"], "1", "2", ["20200102", "2212"], "42")
    for version in ("4", 4):
        segment = SegmentFactory.create_segment("UNB", *elements, version=version)
        assert type(segment) is v4.UNBSegment


def test_getitem_out_of_range_returns_none():
    seg = Segment("FTX", "a")
    assert seg[0] == "a"
    assert seg[-1] == "a"
    assert seg[100] is None
    assert seg[-100] is None


def test_validate_directory_outside_package_raises():
    seg = Segment("BGM", ["380"], "1")
    with pytest.raises(ValueError):
        seg.validate(syntax_version="1", directory="../..")


# PAC 7224 (PackageQuantity) is n..8
@pytest.mark.parametrize("value", ["-2", "1,5", "1.5", "0000", "-0,5", "12345678"])
def test_numeric_element_accepts_iso9735_values(value):
    Segment("PAC", value).validate(syntax_version="4", directory="d24a")


# sign and decimal mark do not count towards the length
def test_numeric_element_length_excludes_sign_and_decimal_mark():
    Segment("PAC", "-1234567,8").validate(syntax_version="4", directory="d24a")
    with pytest.raises(ValidationError):
        Segment("PAC", "-12345678,9").validate(syntax_version="4", directory="d24a")


@pytest.mark.parametrize("value", ["1a", " 2", "2 ", "1,", ",5", "1,2,3", "1-", "--1"])
def test_numeric_element_rejects_non_numeric(value):
    with pytest.raises(ValidationError):
        Segment("PAC", value).validate(syntax_version="4", directory="d24a")


def test_parser_accepts_negative_numeric_element():
    edi = (
        "UNB+UNOA:4+SENDER+RECIPIENT+20240101:1200+REF1'"
        "UNH+1+INVOIC:D:24A:UN'"
        "PAC+-2'"
        "UNT+3+1'"
        "UNZ+1+REF1'"
    )
    assert [s.tag for s in Parser().parse(edi)][2] == "PAC"


# no directory ships a top-level "a" element longer than one character, so use a
# minimal segment definition to exercise the alphabetic check
@pytest.fixture
def alpha_segment_xml(monkeypatch):
    root = ET.fromstring(
        '<segments><segment id="TST">'
        '<data_element id="1" name="Name" repeat="1" type="a" maxlength="35"/>'
        "</segment></segments>"
    )
    monkeypatch.setattr(segments, "_load_segments_xml", lambda directory: root)


def test_alpha_element_allows_space(alpha_segment_xml):
    Segment("TST", "New Zealand").validate(syntax_version="4", directory="d24a")


def test_alpha_element_rejects_digits(alpha_segment_xml):
    with pytest.raises(ValidationError):
        Segment("TST", "Area 51").validate(syntax_version="4", directory="d24a")


# an empty mandatory element is a content error only: the segment layout stays
# intact, so it is accepted with a warning – a missing element still raises
def test_empty_mandatory_element_warns():
    with pytest.warns(NonConformantEDIWarning, match="0062"):
        Segment("UNH", "", ["INVOIC", "D", "24A", "UN"]).validate(
            syntax_version="4", directory="d24a"
        )


def test_missing_mandatory_element_raises():
    with pytest.raises(ValidationError, match="Too few elements"):
        Segment("UNH", "1").validate(syntax_version="4", directory="d24a")
