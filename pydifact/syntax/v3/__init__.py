import pydifact.syntax.common
from pydifact import Segment
from pydifact.syntax import v1, v2

__version__ = 3


class UNASegment(Segment):
    """Service String Advice."""

    version = __version__


class UNBSegment(v1.UNBSegment):
    version = __version__
