#    pydifact - a python edifact library
#    Copyright (C) 2017-2024  Christian González
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

from pydifact.token import Token, TokenType
from pydifact.tokenizer import Tokenizer

from pydifact.control import Characters


@pytest.fixture
def tokenizer() -> Tokenizer:
    return Tokenizer()


def _assert_tokens(
    collection: str,
    expected: list | None = None,
    error_message: str | None = None,
) -> None:
    """Helper function to accelerate tokenizer testing."""

    if expected is None:
        expected = []
    tokens = list(Tokenizer().get_tokens(collection))
    if error_message:
        assert expected == tokens, error_message
    else:
        assert expected == tokens


def test_basic():
    _assert_tokens(
        "RFF+PD:50515'",
        [
            Token(TokenType.CONTENT, "RFF"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "PD"),
            Token(TokenType.COMPONENT_SEPARATOR, ":"),
            Token(TokenType.CONTENT, "50515"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


def test_escape():
    _assert_tokens(
        "RFF+PD?:5'",
        [
            Token(TokenType.CONTENT, "RFF"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "PD:5"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


def test_double_escape():
    _assert_tokens(
        "RFF+PD??:5'",
        [
            Token(TokenType.CONTENT, "RFF"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "PD?"),
            Token(TokenType.COMPONENT_SEPARATOR, ":"),
            Token(TokenType.CONTENT, "5"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


def test_triple_escape():
    _assert_tokens(
        "RFF+PD???:5'",
        [
            Token(TokenType.CONTENT, "RFF"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "PD?:5"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


def test_quadruple_escape():
    _assert_tokens(
        "RFF+PD????:5'",
        [
            Token(TokenType.CONTENT, "RFF"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "PD??"),
            Token(TokenType.COMPONENT_SEPARATOR, ":"),
            Token(TokenType.CONTENT, "5"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


def test_starts_with_escape():
    _assert_tokens(
        "DTM+?+0'",
        [
            Token(TokenType.CONTENT, "DTM"),
            Token(TokenType.DATA_SEPARATOR, "+"),
            Token(TokenType.CONTENT, "+0"),
            Token(TokenType.TERMINATOR, "'"),
        ],
    )


# This tests check if line break combinations (CR/LF) after a segment terminator are correctly ignored.


@pytest.fixture
def expected_crlf():
    return [
        Token(TokenType.CONTENT, "RFF"),
        Token(TokenType.COMPONENT_SEPARATOR, ":"),
        Token(TokenType.CONTENT, "5"),
        Token(TokenType.TERMINATOR, "'"),
        Token(TokenType.CONTENT, "DEF"),
        Token(TokenType.COMPONENT_SEPARATOR, ":"),
        Token(TokenType.CONTENT, "6"),
        Token(TokenType.TERMINATOR, "'"),
    ]


def test_ignore_lf(expected_crlf):
    _assert_tokens("RFF:5'\nDEF:6'", expected_crlf)


def test_ignore_crlf(expected_crlf):
    _assert_tokens("RFF:5'\r\nDEF:6'", expected_crlf)


def test_ignore_cr(expected_crlf):
    _assert_tokens("RFF:5'\rDEF:6'", expected_crlf)


def test_ignore_lfcr(expected_crlf):
    _assert_tokens("RFF:5'\n\rDEF:6'", expected_crlf)


def test_ignore_lfcr_combined(expected_crlf):
    _assert_tokens("RFF:5'\n\r\n\r\nDEF:6'\n\r", expected_crlf)


def test_ignore_whitespace(expected_crlf):
    _assert_tokens("RFF:5'   \nDEF:6'", expected_crlf)


def test_ignore_long_whitespace(expected_crlf):
    _assert_tokens("RFF:5'               \nDEF:6'", expected_crlf)


def test_no_terminator():
    with pytest.raises(RuntimeError):
        list(Tokenizer().get_tokens("TEST", Characters()))
        pytest.fail("Unexpected end of EDI message")
