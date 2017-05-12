#    pydifact - a python edifact library
#    Copyright (C) 2017  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pydifact.Segment import Segment
from pydifact.Serializer import Serializer
import unittest


class SerializerTest(unittest.TestCase):

    def setUp(self):
        self.serializer = Serializer()

    def assertSegments(self, expected: str, segments: list):
        expected = "UNA:+,? '" + expected + "'"
        message = self.serializer.serialize(segments)
        self.assertEqual(expected, message)

    def testBasic1(self):
        self.assertSegments("RFF+PD:50515", [
            Segment("RFF", ["PD", "50515"]),
        ])

    def testBasic2(self):
        self.assertSegments("RFF+PD+50515", [
            Segment("RFF", "PD", "50515"),
        ])

    def testEscapeCharacter(self):
        self.assertSegments("ERC+10:The message does not make sense??", [
            Segment("ERC", ["10", "The message does not make sense?"]),
        ])

    def testEscapeComponentSeparator(self):
        self.assertSegments("ERC+10:Name?: Craig", [
            Segment("ERC", ["10", "Name: Craig"]),
        ])

    def testEscapeDataSeparator(self):
        self.assertSegments("DTM+735:?+0000:406", [
            Segment("DTM", ["735", "+0000", "406"]),
        ])

    def testEscapeDecimalPoint(self):
        self.assertSegments("QTY+136:12,235", [
            Segment("QTY", ["136", "12,235"]),
        ])

    def testEscapeSegmentTerminator(self):
        self.assertSegments("ERC+10:Craig?'s", [
            Segment("ERC", ["10", "Craig's"]),
        ])

    def testEscapeSequence(self):
        self.assertSegments("ERC+10:?:?+???' - ?:?+???' - ?:?+???'", [
            Segment("ERC", ["10", ":+?' - :+?' - :+?'"]),
        ])


if __name__ == '__main__':
    unittest.main()
