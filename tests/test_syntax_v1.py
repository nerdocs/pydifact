from pydifact import Serializer, Parser
from pydifact.exceptions import ValidationError, EDISyntaxError
from pydifact.segments import Segment
import pytest

from pydifact.syntax.v1.segments import UNASegment

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


def test_syntax_v1_requires_una_segment_when_absent():
    """In EDIFACT syntax version 1, a UNA segment is mandatory.

    Ensure that parsing a message without an initial UNA segment raises
    an EDISyntaxError when edi_version=1 is used.
    """

    parser = Parser(edi_version=1)

    # A minimal message starting with UNB and without any preceding UNA
    message_without_una = "UNB+SENDER:1+RECEIVER+950402+1200+1'"

    with pytest.raises(EDISyntaxError):
        # Materialize the iterator to trigger parsing
        list(parser.parse(message_without_una))
