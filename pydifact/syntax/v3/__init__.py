import pydifact.syntax.common
import pydifact.syntax.v1.segments
from pydifact import Segment
from pydifact.syntax import v1, v2

__version__ = 3


class UNASegment(Segment):
    """Service String Advice."""

    version = __version__


class UNBSegment(pydifact.syntax.v1.segments.UNBSegment):
    version = __version__
