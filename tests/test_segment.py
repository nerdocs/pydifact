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

from pydifact.exceptions import MissingImplementationWarning, NonConformantEDIWarning
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

    assert TestSegment in Segment.plugins


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
