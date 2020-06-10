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
import unittest

from pydifact.control import Characters
from pydifact.segmentcollection import SegmentCollection

class TestUNBSegment(unittest.TestCase):
    def setUp(self):
        self.unb_segment = "UNB+UNOA:4+APIS*ABE+USADHS+070429:0900+000000001++USADHS'"
        self.cc = Characters()
        self.cc = self.cc.with_control_character("decimal_point", ".")
        self.collection = SegmentCollection.from_str(self.unb_segment)
        

    def test_una_decimal_point(self):
        self.assertEqual(self.cc.decimal_point, ".")

    def test_unb_segement(self):
        segment = self.collection.segments[0]
        self.assertEqual(segment.tag, 'UNB')
        self.assertEqual(segment.elements[0][0], 'UNOA')
        self.assertEqual(segment.elements[0][1], '4')
        self.assertEqual(segment.elements[1], 'APIS*ABE')
        self.assertEqual(segment.elements[2], 'USADHS')
        self.assertEqual(segment.elements[3][0], '070429')
        self.assertEqual(segment.elements[3][1], '0900')
        self.assertEqual(segment.elements[4], '000000001')
        self.assertEqual(segment.elements[5], '')
        self.assertEqual(segment.elements[6], 'USADHS')
