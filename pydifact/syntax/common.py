import re

from pydifact import Segment, Characters


def assert_n(s, length):
    """checks if s is numeric and has a given length."""
    assert int(s)
    assert len(s) == length


def assert_n_max(s, length):
    """checks if s is numeric and has a given length."""
    assert int(s)
    assert len(s) <= length


def assert_an(s, length):
    """checks if s is alphanumeric and has a given length."""
    assert len(s) == length


def assert_an_max(s, length):
    """checks if s is alphanumeric and has a given length."""
    assert len(s) <= length


def assert_a(s, length):
    """checks if s only contains characters (no numbers) and has a given length."""
    assert len(s) == length
    # TODO only alpha


def assert_a_max(s, length):
    """checks if s only contains characters (no numbers) and has a given length."""
    assert len(s) <= length


def assert_format(s, fmt_str):
    assert re.match(fmt_str, s)


class UNASegment(Segment):
    """Service String Advice."""

    def __init__(self, characters: Characters or str = None):
        if not characters:
            characters = Characters()
        assert_an(str(characters), 6)
        super().__init__("UNA", characters)


class InterchangeHeader:
    def __init__(self, syntax_identifier, version, sender, recipient, date, time):

        assert_n(syntax_identifier, 4)
        assert_n(version, 1)

        assert_an_max(sender, 35)

        assert_n(date, 6)
        assert_n(time, 4)
