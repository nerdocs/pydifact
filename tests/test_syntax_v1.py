from pydifact.segments import Segment
from pydifact.syntax.common import UNASegment

default_characters = ":+,? '"


def test_empty_UNASegment():
    s = UNASegment()
    assert s == Segment("UNA", default_characters)


# TODO: add more checks
