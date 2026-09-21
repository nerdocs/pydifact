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
"""Malformed input must always surface as EDISyntaxError.

Callers only catch `EDISyntaxError`/`ValidationError`, so no malformed interchange
may escape as StopIteration, IndexError, ValueError or AssertionError.
"""

import pytest

from pydifact.exceptions import EDISyntaxError
from pydifact.parser import Parser
from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment

HEADER = "UNB+UNOA:4+SENDER+RECIPIENT+20240101:1200+REF1'"


def test_empty_string():
    with pytest.raises(EDISyntaxError):
        Interchange.from_str("")


def test_una_without_unb():
    with pytest.raises(EDISyntaxError):
        Interchange.from_str("UNA:+.? '")


def test_unb_without_elements():
    with pytest.raises(EDISyntaxError):
        list(Parser(validate=False).parse("UNB'"))


def test_unb_with_too_few_elements():
    with pytest.raises(EDISyntaxError):
        Interchange.from_str("UNB+UNOA:4+S+R'UNZ+0+1'", validate=False)


def test_unb_with_invalid_date():
    with pytest.raises(EDISyntaxError):
        Interchange.from_str("UNB+UNOA:4+S+R+99999999:1200+REF'UNZ+0+REF'")


def test_unh_with_non_composite_message_type():
    with pytest.raises(EDISyntaxError):
        list(
            Interchange.from_str(
                HEADER + "UNH+1+ORDERS'UNT+2+1'UNZ+1+REF1'", validate=False
            ).get_messages()
        )


def test_unh_without_elements():
    with pytest.raises(EDISyntaxError):
        list(
            Interchange.from_str(
                HEADER + "UNH'UNT+2+1'UNZ+1+REF1'", validate=False
            ).get_messages()
        )


def test_una_segment_with_composite_element():
    interchange = Interchange.from_str(HEADER + "UNZ+0+REF1'", validate=False)
    with pytest.raises(EDISyntaxError):
        interchange.add_segment(Segment("UNA", ["a", "b"]))
