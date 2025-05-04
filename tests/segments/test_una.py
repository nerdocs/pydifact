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


from pydifact import Segment
from pydifact.syntax.v1 import UNASegment


def test_compare_against_str():
    u = UNASegment(":+.? '")
    assert str(u) == "'UNA' EDI segment: [ ServiceStringAdvice: ':+.? '']"
    u = UNASegment("123456")
    assert str(u) == "'UNA' EDI segment: [ ServiceStringAdvice: '123456']"


def test_compare_against_same_segment():
    assert UNASegment(":+.? '") == UNASegment(":+.? '")
    assert UNASegment("123456") == UNASegment("123456")


def test_compare_against_other_segment():
    assert UNASegment(":+.? '") != UNASegment("123456")
    # change single chars
    assert UNASegment(":+.? '") != UNASegment(":+.? `")  # backtick!
    assert UNASegment(":+.? '") != UNASegment(";+.? `")  # colon


def test_compare_against_other_segment_type():
    assert UNASegment(":+.? '") != Segment("FOO", "123456")
