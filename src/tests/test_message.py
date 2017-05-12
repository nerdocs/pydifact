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

from pydifact.Message import Message
from pydifact.Segment import Segment
import unittest


class MessageTest(unittest.TestCase):

    def testFromFile(self):

        with self.assertRaises(FileNotFoundError):
            Message.fromFile("/no/such/file")

    def testCreateWithSegments(self):

        message = Message.fromSegments([Segment("36CF")])
        self.assertEqual([
            Segment("36CF"),
        ], message.getAllSegments())

    def testGetSegments(self):

        message = Message.fromSegments([
            Segment("36CF", 1),
            Segment("CPD"),
            Segment("36CF", 2)
        ])
        segments = list(message.getSegments("36CF"))
        self.assertEqual([
            Segment("36CF", 1),
            Segment("36CF", 2),
        ], segments)

    def testGetSegmentsDoesntExist(self):

        message = Message()
        segments = list(message.getSegments("36CF"))
        self.assertEqual([], segments)

    def testGetSegment(self):

        message = Message.fromSegments([
            Segment("36CF", 1),
            Segment("36CF", 2),
        ])
        segment = message.getSegment("36CF")
        self.assertEqual(Segment("36CF", 1), segment)

    def testGetSegmentDoesntExist(self):

        message = Message()
        segment = message.getSegment("36CF")
        self.assertIsNone(segment)
