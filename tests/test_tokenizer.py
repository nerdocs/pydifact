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
import pytest

from pydifact.token import Token
from pydifact.tokenizer import Tokenizer
import unittest

from pydifact.control import Characters


@pytest.fixture
def tokenizer():
    return Tokenizer()


def _assert_tokens(message: str, expected: list = None) -> None:
    if expected is None:
        expected = []
    tokens = Tokenizer().get_tokens("{}'".format(message), Characters())
    expected.append(Token(Token.Type.TERMINATOR, "'"))
    assert expected == tokens


def test_basic():
    _assert_tokens(
        "RFF+PD:50515",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.DATA_SEPARATOR, "+"),
            Token(Token.Type.CONTENT, "PD"),
            Token(Token.Type.COMPONENT_SEPARATOR, ":"),
            Token(Token.Type.CONTENT, "50515"),
        ],
    )


def test_escape():
    _assert_tokens(
        "RFF+PD?:5",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.DATA_SEPARATOR, "+"),
            Token(Token.Type.CONTENT, "PD:5"),
        ],
    )


def test_double_escape():
    _assert_tokens(
        "RFF+PD??:5",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.DATA_SEPARATOR, "+"),
            Token(Token.Type.CONTENT, "PD?"),
            Token(Token.Type.COMPONENT_SEPARATOR, ":"),
            Token(Token.Type.CONTENT, "5"),
        ],
     )


def test_triple_escape():
    _assert_tokens(
        "RFF+PD???:5",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.DATA_SEPARATOR, "+"),
            Token(Token.Type.CONTENT, "PD?:5"),
        ],
    )


def test_quadruple_escape():
    _assert_tokens(
        "RFF+PD????:5",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.DATA_SEPARATOR, "+"),
            Token(Token.Type.CONTENT, "PD??"),
            Token(Token.Type.COMPONENT_SEPARATOR, ":"),
            Token(Token.Type.CONTENT, "5"),
        ],
    )


def test_ignore_whitespace():
    _assert_tokens(
        "RFF:5'\nDEF:6",
        [
            Token(Token.Type.CONTENT, "RFF"),
            Token(Token.Type.COMPONENT_SEPARATOR, ":"),
            Token(Token.Type.CONTENT, "5"),
            Token(Token.Type.TERMINATOR, "'"),
            Token(Token.Type.CONTENT, "DEF"),
            Token(Token.Type.COMPONENT_SEPARATOR, ":"),
            Token(Token.Type.CONTENT, "6"),
        ],
    )


def test_no_terminator():
    with pytest.raises(RuntimeError):
        Tokenizer().get_tokens("TEST", Characters())
        pytest.fail("Unexpected end of EDI message")
