from pydifact.control import Characters
from .common import assert_a, assert_n, assert_an_max, assert_an
from ..segments import Segment


class UNASegment(Segment):
    """Service String Advice."""

    def __init__(self, characters: Characters or str = None):
        if not characters:
            characters = Characters()
        assert len(str(characters)) == 6
        super().__init__("UNA", characters)
