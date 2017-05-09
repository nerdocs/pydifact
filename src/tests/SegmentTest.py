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
import unittest

class SegmentTest(unittest.TestCase):

    def testGetName(self):
        segment = Segment("OMD")
        self.assertEqual("OMD", segment.getName())

    def testGetAllElements(self):
        elements = [
            "field1",
            ["field2", "extra"],
            "stuff",
        ]
        segment = Segment("OMD", elements)
        self.assertEqual(elements, segment.getAllElements())

    def testGetElement1(self):
        elements = [
            "field1",
            ["field2", "extra"],
            "stuff",
        ]
        segment = Segment("OMD", elements)
        self.assertEqual("field1", segment.getElement(0))

    def testGetElement2(self):
        elements = [
            "field1",
            ["field2", "extra"],
            "stuff",
        ]
        segment = Segment("OMD", elements)
        self.assertEqual(["field2", "extra"], segment.getElement(1))

    def testGetElement3(self):
        elements = [
            "field1",
            ["field2", "extra"],
            "stuff",
        ]
        segment = Segment("OMD", elements)
        self.assertIsNone(segment.getElement(7))


if __name__ == '__main__':
    unittest.main()