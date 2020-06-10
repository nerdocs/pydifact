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

class TestUNASegment(unittest.TestCase):
    def setUp(self):
        test_segment = "UNA:+.? '"
        self.cc = Characters.from_str(test_segment)
        

    def test_una_sgement(self):
        self.assertEqual(self.cc.component_separator, ":")
        self.assertEqual(self.cc.data_separator, "+")
        self.assertEqual(self.cc.decimal_point, ".")
        self.assertEqual(self.cc.escape_character, "?")
        self.assertEqual(self.cc.reserved_character, " ")
        self.assertEqual(self.cc.segment_terminator, "'")