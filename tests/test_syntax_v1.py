import pytest

from pydifact import Serializer
from pydifact.exceptions import ValidationError
from pydifact.segments import Segment
from pydifact.syntax.v1 import UNASegment

default_characters = ":+,? '"

# testing the UNASegment class


def test_empty_UNASegment():
    s = UNASegment()
    assert s == Segment("UNA", default_characters)


def test_custom_UNASegment():
    custom_chars = "!@#$% "
    s = UNASegment(custom_chars)
    assert s == Segment("UNA", custom_chars)


def test_UNASegment_str():
    s = UNASegment()
    assert Serializer().serialize([s]) == f"UNA{default_characters}"


def test_invalid_characters_length():
    with pytest.raises(ValidationError):
        una = UNASegment("abc")  # Too short
        una.validate()

    with pytest.raises(ValidationError):
        una = UNASegment("abcdefgh")  # Too long
        una.validate()


def test_UNASegment_characters():
    s = UNASegment(":+,? '")
    assert s.component_separator == ":"
    assert s.data_separator == "+"
    assert s.decimal_point == ","
    assert s.escape_character == "?"
    assert s.reserved_character == " "
    assert s.segment_terminator == "'"
