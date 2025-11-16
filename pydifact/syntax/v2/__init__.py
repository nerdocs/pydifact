__version__ = 2

from pydifact import Segment, Characters
from pydifact.syntax import v1


class UNASegment(Segment):
    """Service String Advice."""

    version = __version__

    def __init__(self, characters: Characters | str | None = None):  # noqa
        super().__init__()
        # in this special case, we need no super class, as we directly set the
        # Character string
        if isinstance(characters, str):
            characters = Characters.from_str(characters)
        else:
            characters = Characters() if characters is None else characters
        self.elements = [str(characters)]
        # provide shortcut handles to the separators
        self.component_separator = characters.component_separator
        self.data_separator = characters.data_separator
        self.decimal_point = characters.decimal_point
        self.escape_character = characters.escape_character
        self.reserved_character = characters.reserved_character
        self.segment_terminator = characters.segment_terminator
