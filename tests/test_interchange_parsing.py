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

from pydifact.control.characters import Characters
from pydifact.exceptions import EDISyntaxError, ValidationError
from pydifact.parser import Parser
from pydifact.segmentcollection import Interchange, RawSegmentCollection


@pytest.fixture
def interchange_str():
    return (
        "UNB+UNOC:1+1234+3333+200102:2212+42'"
        "UNH+42z42+PAORES:93:1:IA'"
        "UNT+2+42z42'"
        "UNZ+1+42'"
    )


def test_from_str(interchange_str):
    i = Interchange.from_str(interchange_str)
    assert str(i) == interchange_str


def test_from_str_with_una(interchange_str):
    i = Interchange.from_str("UNA:+,? '" + interchange_str)
    assert i.has_una_segment


def test_with_custom_decimal_separator(interchange_str):
    i = Interchange.from_str("UNA:+.? '" + interchange_str)
    assert i.characters.decimal_point == "."


def test_with_default_parser(interchange_str):
    i = Interchange.from_str(interchange_str, parser=Parser())
    assert str(i) == interchange_str


def test_configured_parser_and_una(interchange_str):
    parser = Parser(characters=Characters.from_str("UNA:+.? '"))

    i = Interchange.from_str("UNA:+.? '" + interchange_str, parser=parser)
    assert i.characters.decimal_point == "."


def test_configured_parser_and_differing_una(interchange_str):
    parser = Parser(characters=Characters.from_str("UNA:+.? '"))

    i = Interchange.from_str("UNA:+,? '" + interchange_str, parser=parser)
    assert i.characters.decimal_point == ","


def test_configured_parser_and_no_una(interchange_str):
    parser = Parser(characters=Characters.from_str("UNA:+.? '"))

    i = Interchange.from_str(interchange_str, parser=parser)
    assert i.characters.decimal_point == "."


# UNH message reference number (0062) is limited to an..14
INVALID_UNH = "UNH+123456789012345+PAORES:93:1:IA'"
# UNB interchange control reference (0020) is limited to an..14
INVALID_UNB = "UNB+UNOC:1+1234+3333+200102:2212+123456789012345'"
# segments are only validated after UNB has set the syntax version
VALID_UNB = "UNB+UNOC:1+1234+3333+200102:2212+42'"


def test_invalid_segment_raises_by_default():
    with pytest.raises(ValidationError):
        Interchange.from_str(VALID_UNB + INVALID_UNH)


def test_invalid_segment_without_validation():
    i = Interchange.from_str(VALID_UNB + INVALID_UNH, validate=False)
    assert i.segments[0].elements[0] == "123456789012345"


def test_invalid_unb_raises_by_default():
    with pytest.raises(ValidationError):
        Interchange.from_str(INVALID_UNB)


def test_invalid_unb_without_validation():
    i = Interchange.from_str(INVALID_UNB, validate=False)
    assert i.control_reference == "123456789012345"


def test_invalid_unb_with_non_validating_parser():
    # the parser skips segment validation, but the UNB header is still validated
    with pytest.raises(EDISyntaxError, match="Invalid UNB header"):
        Interchange.from_str(INVALID_UNB, parser=Parser(validate=False))


def test_from_file_without_validation(tmp_path):
    edi_file = tmp_path / "invalid.edi"
    edi_file.write_text(INVALID_UNB + INVALID_UNH, encoding="iso8859-1")

    with pytest.raises(ValidationError):
        Interchange.from_file(str(edi_file))

    i = Interchange.from_file(str(edi_file), validate=False)
    assert i.control_reference == "123456789012345"
    assert i.segments[0].elements[0] == "123456789012345"


def test_raw_segment_collection_without_validation():
    with pytest.raises(ValidationError):
        RawSegmentCollection.from_str(VALID_UNB + INVALID_UNH)

    collection = RawSegmentCollection.from_str(VALID_UNB + INVALID_UNH, validate=False)
    assert [s.tag for s in collection.segments] == ["UNB", "UNH"]
