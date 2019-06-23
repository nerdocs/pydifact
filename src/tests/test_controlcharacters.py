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


class TestControlCharacters(unittest.TestCase):
    def setUp(self):
        self.cc = Characters()

    def test_wrong_attribute(self):
        self.assertRaises(
            AttributeError, self.cc.with_control_character, "wrongtype", "+"
        )

    def test_wrong_character_size(self):
        self.assertRaises(
            ValueError, self.cc.with_control_character, "decimal_point", ",."
        )

    def test_correct_parameters(self):

        d = self.cc.with_control_character("component_separator", "/")

        self.assertEqual(
            self.cc.with_control_character(
                "component_separator", "/"
            ).component_separator,
            "/",
        )

        self.assertEqual(
            self.cc.with_control_character("data_separator", "/").data_separator, "/"
        )

        self.assertEqual(
            self.cc.with_control_character("decimal_point", "/").decimal_point, "/"
        )

        self.assertEqual(
            self.cc.with_control_character("escape_character", "/").escape_character,
            "/",
        )

        self.assertEqual(
            self.cc.with_control_character(
                "reserved_character", "/"
            ).reserved_character,
            "/",
        )

        self.assertEqual(
            self.cc.with_control_character(
                "segment_terminator", "/"
            ).segment_terminator,
            "/",
        )
