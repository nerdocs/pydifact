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
from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.tokenizer import Tokenizer

import unittest
from unittest import mock

from pydifact.control import Characters


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.default_una_segment = Segment('UNA', ":+,? '")

    @mock.patch('pydifact.Tokenizer.Tokenizer')
    def get_control_characters(self, message: str, tokenizer=None) -> Characters:
        """Returns the control characters from the given message.

        :return: the message without the "UNA123456" header string
        """

        if tokenizer is None:
            tokenizer = mock.MagicMock(spec=Tokenizer)
            tokenizer.set_control_character.assert_called_once_with("set_component_separator", 1)
            tokenizer.set_control_character.assert_called_once_with("set_data_separator", 2)
            tokenizer.set_control_character.assert_called_once_with("set_decimal_point", 3)
            tokenizer.set_control_character.assert_called_once_with("set_escape_character", 4)
            tokenizer.set_control_character.assert_called_once_with("set_segment_terminator", 6)
        # FIXME: use characters
        return self.parser.get_control_characters(message, tokenizer)

#    def test_setup_special_characters1(self):
#
#        tokenizer = mock.MagicMock(spec=Tokenizer)
#        message = self.get_control_characters("TEST", tokenizer)
#        self.assertEqual("TEST", message)

    def test_setup_special_characters2(self):

        message = self.get_control_characters("UNA123456")
        self.assertEqual("", message)

    def test_setup_special_characters3(self):

        message = self.get_control_characters("UNA123456TEST")
        self.assertEqual("TEST", message)

    def test_setup_special_characters4(self):

        message = self.get_control_characters("UNA123456\nTEST")
        self.assertEqual("TEST", message)

    def test_setup_special_characters5(self):

        message = self.get_control_characters("UNA123456\r\nTEST")
        self.assertEqual("TEST", message)

    def _assert_segments(self, message: str, segments: list):
        """This function asserts that the given message, when parsed with
        Parser.parse(), produces exactly the list output given by segments.
        :param message: The message to parse. The UNA string is added.
        :param segments: The expected segments list
        """

        input_str = "UNA:+,? '\n" + message + "'\n"
        result = list(self.parser.parse(input_str))
        print("input segments: {}".format(segments[0]))
        print("parser result:  {}".format(result[0]))
        self.assertCountEqual([self.default_una_segment] + segments, result)

    def test_compare_equal_segments(self):
        """Just make sure that comparing Segment objects works"""
        a = [Segment("RFF", ["PD", "50515"])]
        b = [Segment("RFF", ["PD", "50515"])]
        assert a is not b, \
            "Two separatedly created Segment objects may not be a singleton."
        self.assertEqual(a, b)

    def test_una_parser1(self):
        # UNA headers are a special parsing task and must be processed correctly.
        tokens = self.parser.parse("UNA:+,? 'TEST'")
        self.assertEqual(next(tokens), Segment('UNA', ":+,? '"))
        self.assertEqual(next(tokens), Segment('TEST'))

    def test_una_parser2(self):
        # UNA headers are a special parsing task and must be processed correctly.
        tokens = self.parser.parse("UNA123456TEST6")
        self.assertEqual(next(tokens), Segment('UNA', "123456"))
        self.assertEqual(next(tokens), Segment('TEST'))

    def test_una_parser3(self):
        # UNA headers are a special parsing task and must be processed correctly.
        tokens = self.parser.parse("UNA12345'TEST'")
        self.assertEqual(next(tokens), Segment('UNA', "12345'"))
        self.assertEqual(next(tokens), Segment('TEST'))

    def test_basic1(self):

        self._assert_segments("RFF+PD:50515", [
            Segment("RFF", ["PD", "50515"]),
        ])

    def test_basic2(self):

        self._assert_segments("RFF+PD+50515", [
            Segment("RFF", "PD", "50515"),
        ])

    def test_escape_character(self):

        self._assert_segments("ERC+10:The message does not make sense??", [
            Segment("ERC", ["10", "The message does not make sense?"]),
        ])

    def test_escape_component_separator(self):

        self._assert_segments("ERC+10:Name?: Craig", [
            Segment("ERC", ["10", "Name: Craig"]),
        ])

    def test_escape_data_separator(self):

        self._assert_segments("DTM+735:?+0000:406", [
            Segment("DTM", ["735", "+0000", "406"]),
        ])

    def test_escape_decimal_point(self):

        self._assert_segments("QTY+136:12,235", [
            Segment("QTY", ["136", "12,235"]),
        ])

    def test_escape_segment_terminator(self):

        self._assert_segments("ERC+10:Craig?'s", [
            Segment("ERC", ["10", "Craig's"]),
        ])

    def test_escape_sequence(self):

        self._assert_segments("ERC+10:?:?+???' - ?:?+???' - ?:?+???'", [
            Segment("ERC", ["10", ":+?' - :+?' - :+?'"]),
        ])


if __name__ == '__main__':
    unittest.main()
