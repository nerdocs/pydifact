import re
from typing import Literal


def edifact_syntax_version(directory: str) -> Literal[1, 2, 3, 4]:
    """
    Returns the EDIFACT syntax version (1–4) for a directory like 'D96A'.

    It accepts the following formats (case insensitive):
    * d96a, D96A, D.96A, D96B, ...
    * 91-2, 88-2


    https://unece.org/trade/uncefact/unedifact/download
    """

    directory = directory.upper().replace(".", "")

    # extract year
    if re.match(r"D\d{2}[AB]", directory):
        year = int(directory[1:3])
    elif re.match(r"D?\d{2}-\d", directory):
        year = int(directory.split("-")[0])
    else:
        raise ValueError("Invalid EDIFACT directory format")

    # Syntax mapping
    if 87 <= year <= 88:
        return 1
    elif 89 <= year <= 92:
        return 2
    elif 93 <= year <= 99:
        return 3
    elif 0 <= year <= 24:  # D00A - D24A ++.
        return 4
    else:
        raise ValueError("Unknown EDIFACT directory year")


def edifact_syntax_directory(syntax_version: int) -> str:
    """
    Returns the latest EDIFACT syntax directory (like 'D24A') for a given
    syntax version (1–4).
    """
    # Syntax mapping
    if syntax_version == 1:
        return "D88"
    elif syntax_version == 2:
        return "D92A"
    elif syntax_version == 3:
        return "D99B"
    elif syntax_version == 4:
        return "D24A"

    raise ValueError("Unknown EDIFACT syntax version")


def is_valid_syntax_directory(directory: str) -> bool:
    """
    Returns True if the given directory is a valid EDIFACT syntax directory.
    """
    try:
        return edifact_syntax_version(directory) is not None
    except ValueError:  # unknown directory format / year
        return False
