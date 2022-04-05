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

import pytest

# @pytest.fixture
# def mocked_tokenizer(mocker):
#     tokenizer = Tokenizer()
#     mocker.patch("pydifact.tokenizer.Tokenizer")
#     return tokenizer


@pytest.fixture
def parser():
    return Parser()


@pytest.fixture
def default_una_segment():
    return Segment("UNA", ":+,? '")


# def get_control_characters(mocker, parser, collection: str, tokenizer=None) -> Characters:
#     """Returns the control characters from the given collection.
#
#     :return: the collection without the "UNA123456" header string
#     """
#
#     if tokenizer is None:
#         mocker.patch("pydifact.tokenizer.Tokenizer")
#         tokenizer = Tokenizer()
#
#         tokenizer.set_control_character.assert_called_once_with(
#             "set_component_separator", 1
#         )
#         tokenizer.set_control_character.assert_called_once_with(
#             "set_data_separator", 2
#         )
#         tokenizer.set_control_character.assert_called_once_with(
#             "set_decimal_point", 3
#         )
#         tokenizer.set_control_character.assert_called_once_with(
#             "set_escape_character", 4
#         )
#         tokenizer.set_control_character.assert_called_once_with(
#             "set_segment_terminator", 6
#         )
#     # FIXME: use characters
#     return parser.get_control_characters(collection, tokenizer)

#    def test_setup_special_characters1(self):
#
#        tokenizer = mock.MagicMock(spec=Tokenizer)
#        collection = self.get_control_characters("TEST", tokenizer)
#        self.assertEqual("TEST", collection)


def test_setup_special_characters_only(parser):
    assert parser.get_control_characters("UNA123456") == "123456"


def test_setup_special_characters_with_message(parser):
    assert parser.get_control_characters("UNA123456TEST") == "123456"


def test_setup_special_characters_with_linefeed(parser):
    assert parser.get_control_characters("UNA123456\nTEST") == "123456"


def test_setup_special_characters_with_crlf(parser):
    assert parser.get_control_characters("UNA123456\r\nTEST") == "123456"


def _assert_segments(parser, default_una_segment, collection: str, segments: list):
    """This function asserts that the given collection, when parsed with
    Parser.parse(), produces exactly the list output given by segments.
    :param collection: The collection to parse. The UNA string is added.
    :param segments: The expected segments list
    """

    input_str = "UNA:+,? '\n" + collection + "'\n"
    result = list(parser.parse(input_str))
    # print("input segments: {}".format(segments[0]))
    # print("parser result:  {}".format(result[0]))
    assert segments == result


def test_compare_equal_segments(parser, default_una_segment):
    """Just make sure that comparing Segment objects works"""
    a = Segment("RFF", ["PD", "50515"])
    b = Segment("RFF", ["PD", "50515"])
    assert a == b
    assert (
        a is not b
    ), "Two separatedly, but visually identically created Segment objects may not be the same object."


def test_una_parser1(parser):
    # UNA headers are a special parsing task and must be processed correctly.
    tokens = parser.parse("UNA:+,? 'TEST'")
    assert next(tokens) == Segment("TEST")


def test_una_parser2(parser):
    # UNA headers are a special parsing task and must be processed correctly.
    tokens = parser.parse("UNA123456TEST6")
    assert next(tokens) == Segment("TEST")


def test_una_parser3(parser):
    # UNA headers are a special parsing task and must be processed correctly.
    tokens = parser.parse("UNA12345'TEST'")
    assert next(tokens) == Segment("TEST")


def test_basic1(parser, default_una_segment):
    _assert_segments(
        parser, default_una_segment, "RFF+PD:50515", [Segment("RFF", ["PD", "50515"])]
    )


def test_basic2(parser, default_una_segment):

    _assert_segments(
        parser, default_una_segment, "RFF+PD+50515", [Segment("RFF", "PD", "50515")]
    )


def test_escape_character(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:The message does not make sense??",
        [Segment("ERC", ["10", "The message does not make sense?"])],
    )


def test_escape_component_separator(parser, default_una_segment):

    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:Name?: Craig",
        [Segment("ERC", ["10", "Name: Craig"])],
    )


def test_escape_data_separator(parser, default_una_segment):

    _assert_segments(
        parser,
        default_una_segment,
        "DTM+735:?+0000:406",
        [Segment("DTM", ["735", "+0000", "406"])],
    )


def test_escape_decimal_point(parser, default_una_segment):

    _assert_segments(
        parser,
        default_una_segment,
        "QTY+136:12,235",
        [Segment("QTY", ["136", "12,235"])],
    )


def test_escape_segment_terminator(parser, default_una_segment):

    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:Craig?'s",
        [Segment("ERC", ["10", "Craig's"])],
    )


def test_escape_sequence(parser, default_una_segment):

    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:?:?+???' - ?:?+???' - ?:?+???'",
        [Segment("ERC", ["10", ":+?' - :+?' - :+?'"])],
    )


def test_compound_starts_with_skipped(parser, default_una_segment):

    _assert_segments(
        parser, default_una_segment, "IMD+::A", [Segment("IMD", ["", "", "A"])]
    )


def test_compound_contains_one_skipped(parser, default_una_segment):

    _assert_segments(
        parser, default_una_segment, "IMD+A::B", [Segment("IMD", ["A", "", "B"])]
    )


def test_compound_contains_two_skipped(parser, default_una_segment):

    _assert_segments(
        parser, default_una_segment, "IMD+A:::B", [Segment("IMD", ["A", "", "", "B"])]
    )
