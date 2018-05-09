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
from pydifact.message import Message
from pydifact.segments import Segment
import unittest


class MessageTest(unittest.TestCase):

    def test_from_file(self):

        with self.assertRaises(FileNotFoundError):
            Message.from_file("/no/such/file")

    def test_create_with_segments(self):

        message = Message.from_segments([Segment("36CF")])
        self.assertEqual([
            Segment("36CF"),
        ], message.segments)

    def test_get_segments(self):

        message = Message.from_segments([
            Segment("36CF", 1),
            Segment("CPD"),
            Segment("36CF", 2)
        ])
        segments = list(message.get_segments("36CF"))
        self.assertEqual([
            Segment("36CF", 1),
            Segment("36CF", 2),
        ], segments)

    def test_get_segments_doesnt_exist(self):

        message = Message()
        segments = list(message.get_segments("36CF"))
        self.assertEqual([], segments)

    def test_get_segment(self):

        message = Message.from_segments([
            Segment("36CF", 1),
            Segment("36CF", 2),
        ])
        segment = message.get_segment("36CF")
        self.assertEqual(Segment("36CF", 1), segment)

    def test_get_segment_doesnt_exist(self):

        message = Message()
        segment = message.get_segment("36CF")
        self.assertIsNone(segment)


if __name__ == '__main__':
    unittest.main()
