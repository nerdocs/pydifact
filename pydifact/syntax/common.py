from pydifact import Segment, Characters


class UNASegment(Segment):
    """Service String Advice."""

    def __init__(self, characters: Characters or str = None):
        if not characters:
            characters = Characters()
        assert len(str(characters)) == 6
        super().__init__("UNA", characters)


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
