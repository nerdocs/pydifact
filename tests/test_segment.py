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

from pydifact.segments import Segment


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
