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

from pydifact.Token import Token
from pydifact.Tokenizer import Tokenizer
import unittest


class TokenizerTest(unittest.TestCase):

    def setUp(self):
        self._tokenizer = Tokenizer()

    def _assertTokens(self, message, expected=[]):
        tokens = self._tokenizer.getTokens(
            "{message}'".format(message=message))

        expected.append(Token(Token.TERMINATOR, "'"))
        self.assertEqual(expected, tokens)

    def testBasic(self):
        self._assertTokens("RFF+PD:50515", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.DATA_SEPARATOR, "+"),
            Token(Token.CONTENT, "PD"),
            Token(Token.COMPONENT_SEPARATOR, ":"),
            Token(Token.CONTENT, "50515"),
        ])

    def testEscape(self):
        self._assertTokens("RFF+PD?:5", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.DATA_SEPARATOR, "+"),
            Token(Token.CONTENT, "PD:5"),
        ])

    def testDoubleEscape(self):
        self._assertTokens("RFF+PD??:5", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.DATA_SEPARATOR, "+"),
            Token(Token.CONTENT, "PD?"),
            Token(Token.COMPONENT_SEPARATOR, ":"),
            Token(Token.CONTENT, "5"),
        ])

    def testTripleEscape(self):
        self._assertTokens("RFF+PD???:5", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.DATA_SEPARATOR, "+"),
            Token(Token.CONTENT, "PD?:5"),
        ])

    def testQuadrupleEscape(self):
        self._assertTokens("RFF+PD????:5", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.DATA_SEPARATOR, "+"),
            Token(Token.CONTENT, "PD??"),
            Token(Token.COMPONENT_SEPARATOR, ":"),
            Token(Token.CONTENT, "5"),
        ])

    def testIgnoreWhitespace(self):
        self._assertTokens("RFF:5'\nDEF:6", [
            Token(Token.CONTENT, "RFF"),
            Token(Token.COMPONENT_SEPARATOR, ":"),
            Token(Token.CONTENT, "5"),
            Token(Token.TERMINATOR, "'"),
            Token(Token.CONTENT, "DEF"),
            Token(Token.COMPONENT_SEPARATOR, ":"),
            Token(Token.CONTENT, "6"),
        ])

    def testNoTerminator(self):
        with self.assertRaises(RuntimeError) as cm:
            self._tokenizer.getTokens("TEST")
        self.assertEqual(str(cm.exception), "Unexpected end of EDI message")


if __name__ == '__main__':
    unittest.main()
