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


class CharactersTest(unittest.TestCase):

    def test_with_separator_identity(self):
        one = Characters()
        other = Characters()
        # a copy of a characters object must be equal, but not the same
        self.assertTrue(one == other, 'Objects differ: "{}", "{}"'.format(one, other))
        self.assertFalse(one is other)

    def test_cc_assigning(self):
        one = Characters()
        one.component_separator = 'x'
        self.assertEqual(one.component_separator, 'x')
        self.assertEqual(str(one), "x+,? '")

#    def test_wrong_cc_assigning(self):
#        with self.assertRaises(ValueError):
#            Characters().with_control_character(
#                'component_separator', 'xd')
#
#        with self.assertRaises(AttributeError):
#            Characters().with_control_character('notexisting', ':')


if __name__ == '__main__':
    unittest.main()
