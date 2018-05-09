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
from pydifact.segments import Segment
from pydifact.serializer import Serializer
import unittest


class SerializerTest(unittest.TestCase):

    def setUp(self):
        self.serializer = Serializer()

    def assert_segments(self, expected: str, segments: list):
        expected = "UNA:+,? '" + expected + "'"
        message = self.serializer.serialize(segments, with_una=True)
        self.assertEqual(expected, message)

    def test_basic1(self):
        self.assert_segments("RFF+PD:50515", [
            Segment("RFF", ["PD", "50515"]),
        ])

    def test_basic2(self):
        self.assert_segments("RFF+PD+50515", [
            Segment("RFF", "PD", "50515"),
        ])

    def test_escape_character(self):
        self.assert_segments("ERC+10:The message does not make sense??", [
            Segment("ERC", ["10", "The message does not make sense?"]),
        ])

    def test_escape_component_separator(self):
        self.assert_segments("ERC+10:Name?: Craig", [
            Segment("ERC", ["10", "Name: Craig"]),
        ])

    def test_escape_data_separator(self):
        self.assert_segments("DTM+735:?+0000:406", [
            Segment("DTM", ["735", "+0000", "406"]),
        ])

    def test_escape_decimal_point(self):
        self.assert_segments("QTY+136:12,235", [
            Segment("QTY", ["136", "12,235"]),
        ])

    def test_escape_segment_terminator(self):
        self.assert_segments("ERC+10:Craig?'s", [
            Segment("ERC", ["10", "Craig's"]),
        ])

    def test_escape_sequence(self):
        self.assert_segments("ERC+10:?:?+???' - ?:?+???' - ?:?+???'", [
            Segment("ERC", ["10", ":+?' - :+?' - :+?'"]),
        ])


if __name__ == '__main__':
    unittest.main()
