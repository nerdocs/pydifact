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
from pydifact.exceptions import EdifactSyntaxError
from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.control.characters import Characters
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
    # print(f"input segments: {segments[0]}")
    # print(f"parser result:  {result[0]}")
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
    tokens = parser.parse("UNA:+,? 'FOO+TEST'")
    assert next(tokens) == Segment("UNA", ":+,? '")
    assert next(tokens) == Segment("FOO", "TEST")


def test_una_parser2(parser):
    # UNA headers are a special parsing task and must be processed correctly.
    tokens = parser.parse("UNA123456FOO2TEST6")
    assert next(tokens) == Segment("UNA", "123456")
    assert next(tokens) == Segment("FOO", "TEST")


def test_una_parser3(parser):
    # UNA headers are a special parsing task and must be processed correctly.
    tokens = parser.parse("UNA12345'FOO2TEST'")
    assert next(tokens) == Segment("UNA", "12345'")
    assert next(tokens) == Segment("FOO", "TEST")


def test_basic1(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "RFF+PD:50515",
        [Segment("UNA", ":+,? '"), Segment("RFF", ["PD", "50515"])],
    )


def test_basic2(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "RFF+PD+50515",
        [Segment("UNA", ":+,? '"), Segment("RFF", "PD", "50515")],
    )


def test_escape_character(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:The message does not make sense??",
        [
            Segment("UNA", ":+,? '"),
            Segment("ERC", ["10", "The message does not make sense?"]),
        ],
    )


def test_escape_component_separator(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:Name?: Craig",
        [Segment("UNA", ":+,? '"), Segment("ERC", ["10", "Name: Craig"])],
    )


def test_escape_data_separator(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "DTM+735:?+0000:406",
        [Segment("UNA", ":+,? '"), Segment("DTM", ["735", "+0000", "406"])],
    )


def test_escape_decimal_point(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "QTY+136:12,235",
        [Segment("UNA", ":+,? '"), Segment("QTY", ["136", "12,235"])],
    )


def test_escape_segment_terminator(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:Craig?'s",
        [Segment("UNA", ":+,? '"), Segment("ERC", ["10", "Craig's"])],
    )


def test_escape_sequence(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "ERC+10:?:?+???' - ?:?+???' - ?:?+???'",
        [Segment("UNA", ":+,? '"), Segment("ERC", ["10", ":+?' - :+?' - :+?'"])],
    )


def test_compound_starts_with_skipped(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "IMD+::A",
        [Segment("UNA", ":+,? '"), Segment("IMD", ["", "", "A"])],
    )


def test_compound_contains_one_skipped(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "IMD+A::B",
        [Segment("UNA", ":+,? '"), Segment("IMD", ["A", "", "B"])],
    )


def test_compound_contains_two_skipped(parser, default_una_segment):
    _assert_segments(
        parser,
        default_una_segment,
        "IMD+A:::B",
        [Segment("UNA", ":+,? '"), Segment("IMD", ["A", "", "", "B"])],
    )


def test_parsing_with_new_default_characters():
    parser = Parser(characters=Characters.from_str("UNA:+,! '"))
    segments = parser.parse("ERC+10:Craig!'s'")
    assert [s for s in segments] == [
        Segment("ERC", ["10", "Craig's"]),
    ]


def test_parsing_with_passed_characters_():
    parser = Parser()
    segments = parser.parse(
        "ERC+10:Craig!'s'", characters=Characters.from_str("UNA:+,! '")
    )
    assert [s for s in segments] == [
        Segment("ERC", ["10", "Craig's"]),
    ]


def test_parsing_with_passed_characters_but_respect_una():
    parser = Parser()
    segments = parser.parse(
        "UNA:+,! 'ERC+10:Craig!'s'", characters=Characters.from_str("UNA:+,? '")
    )
    assert [s for s in segments] == [
        Segment("UNA", ":+,! '"),
        Segment("ERC", ["10", "Craig's"]),
    ]


def test_message_end_without_control_char():
    with pytest.raises(EdifactSyntaxError):
        # must raise a RuntimeError as the string terminates abruptly within a segment
        for c in Parser().parse("UNB+IBMA:1+BLUBB A+FOO X+950"):
            pass


def test_edifact_text_with_newlines():
    example_text = """UNB+IBMA:1+FACHARZT A+PRAKTIKER X+950402+1200+1'
UNH+000001+MEDRPT:1:901:UN'
BGM+080+++19950402++123401011967+19670101'
FTX+BFD++Keine Wachstumsstörungen.:'
NAD+PAT++TEST:LIESCHEN:NULLWEG 97:+++NIRGENDWO++0000'
UNT+7+000001'
UNH+000002+MEDRPT:1:901:UN'
BGM+080+++19950402++567802041993+19930402'
FTX+BFD++Ich konnte keine Abnormalitäten entdecken:'
NAD+PAT++TEST:MAX:NULLWEG 98:+++NIRGENDWO++0000'
UNT+7+000002'
UNZ+2+1'"""
    segments = list(Parser().parse(example_text))
    assert len(segments) == 12
    segments = list(Parser().parse("UNA:+,? '" + example_text))
    assert len(segments) == 13
