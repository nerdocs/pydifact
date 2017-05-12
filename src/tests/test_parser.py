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

from pydifact.Parser import Parser
from pydifact.Segment import Segment
from pydifact.Tokenizer import Tokenizer

import unittest
from unittest.mock import patch, MagicMock


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    @patch("pydifact.Tokenizer")
    def setupSpecialCharacters(self,
                               message: str,
                               tokenizer: Tokenizer = None) -> str:
        """
        :return: the message without the "UNA123456" string
        """

        if tokenizer == None:
            tokenizer = MagicMock(spec=Tokenizer)
            tokenizer.setControlCharacter.assert_called_once_with("setComponentSeparator", 1)
            #tokenizer.setControlCharacter.assert_called_once_with("setDataSeparator", 2)
            #tokenizer.setControlCharacter.assert_called_once_with("setDecimalPoint", 3)
            #tokenizer.setControlCharacter.assert_called_once_with("setEscapeCharacter", 4)
            #tokenizer.setControlCharacter.assert_called_once_with("setSegmentTerminator", 6)

        self.parser.setupSpecialCharacters(message, tokenizer)

    def testSetupSpecialCharacters1(self):

        tokenizer = MagicMock(spec=Tokenizer)
        message = self.setupSpecialCharacters("TEST", tokenizer)
        self.assertEqual("TEST", message)

    def testSetupSpecialCharacters2(self):

        message = self.setupSpecialCharacters("UNA123456")
        self.assertEqual("", message)

    def testSetupSpecialCharacters3(self):

        message = self.setupSpecialCharacters("UNA123456TEST")
        self.assertEqual("TEST", message)

    def testSetupSpecialCharacters4(self):

        message = self.setupSpecialCharacters("UNA123456\nTEST")
        self.assertEqual("TEST", message)

    def testSetupSpecialCharacters5(self):

        message = self.setupSpecialCharacters("UNA123456\r\nTEST")
        self.assertEqual("TEST", message)

    def _assertSegments(self, message: str, segments: list):

        input = "UNA:+,? '\n"
        input += message + "'\n"
        result = self.parser.parse(input)
        # FIXME: result = iterator_to_array(result)
        self.assertEqual(segments, result)

    def testBasic1(self):

        self._assertSegments("RFF+PD:50515", [
            Segment("RFF", ["PD", "50515"]),
        ])

    def testBasic2(self):

        self._assertSegments("RFF+PD+50515", [
            Segment("RFF", "PD", "50515"),
        ])

    def testEscapeCharacter(self):

        self._assertSegments("ERC+10:The message does not make sense??", [
            Segment("ERC", ["10", "The message does not make sense?"]),
        ])

    def testEscapeComponentSeparator(self):

        self._assertSegments("ERC+10:Name?: Craig", [
            Segment("ERC", ["10", "Name: Craig"]),
        ])

    def testEscapeDataSeparator(self):

        self._assertSegments("DTM+735:?+0000:406", [
            Segment("DTM", ["735", "+0000", "406"]),
        ])

    def testEscapeDecimalPoint(self):

        self._assertSegments("QTY+136:12,235", [
            Segment("QTY", ["136", "12,235"]),
        ])

    def testEscapeSegmentTerminator(self):

        self._assertSegments("ERC+10:Craig?'s", [
            Segment("ERC", ["10", "Craig's"]),
        ])

    def testEscapeSequence(self):

        self._assertSegments("ERC+10:?:?+???' - ?:?+???' - ?:?+???'", [
            Segment("ERC", ["10", ":+?' - :+?' - :+?'"]),
        ])
