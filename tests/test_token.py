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


def test_type():
    token = Token(TokenType.CONTENT, "ok")
    assert TokenType.CONTENT == token.type


def test_value():
    token = Token(TokenType.CONTENT, "ok")
    assert token.value == "ok"


def test_wrong_type():
    with pytest.raises(TypeError):
        Token(123, "ok")

    with pytest.raises(TypeError):
        Token(True, "ok")
