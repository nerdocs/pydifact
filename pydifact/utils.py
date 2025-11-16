import re
from typing import Literal


def syntax_versions_from_directory(directory: str) -> list[Literal[1, 2, 3, 4]]:
    """
    Matches the given EDIFACT directory identifier to a list of possible syntax versions.
    https://unece.org/trade/uncefact/unedifact/download

    Args:
        directory: The EDIFACT directory identifier (case-insensitive).
            It accepts the following formats:
            * d96a, D96A, D.96A, D96B, D.01C...
            * 91-2, 88-2
    Returns:
        A list of possible EDIFACT syntax versions (1–4) for a directory like 'D96A'.
    """

    versions: list[Literal[1, 2, 3, 4]] = []
    directory = directory.upper().replace(".", "")
    # extract year
    if pattern := re.match(r"^[DS]?\.?(\d{2})-?[ABC]?$", directory):
        year = int(pattern.group(1))
    else:
        raise ValueError("Invalid EDIFACT directory format")

    # Syntax mapping
    if 2 <= year <= 24:  # D00A - D24A ++.
        versions.append(4)
    if 92 <= year <= 99 or 0 <= year <= 2:  # 1992-2002
        versions.append(3)
    if 90 <= year <= 92:
        versions.append(2)
    if 87 <= year <= 90:
        versions.append(1)
    if 24 < year < 87:
        raise ValueError("Unknown EDIFACT directory year")
    return versions


def directory_from_syntax_version(syntax_version: int) -> str:
    """
    Returns the latest EDIFACT syntax directory (like 'D24A') for a given
    syntax version (1–4).

    If syntax_version is not supported, ValueError is raised.
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
        return syntax_versions_from_directory(directory) != []
    except ValueError:  # unknown directory format / year
        return False


allowed_alphanum_chars = set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*-./:()'&=+\"?,"
    "!_\\ "
)


def is_edifact_alphanum(s: str) -> bool:
    """Returns True if str contains only alphanumeric characters in the sense of
    EDIFACT.

    See https://service.gefeg.com/jwg1/Files/V41-9735-1.pdf - page 11
    """
    return all(
        c.isalnum() or (c.isascii() and c.isprintable() and not c.isalnum()) for c in s
    )


def assert_a(s, length, message=""):
    """checks if s consists of only alphabetical characters, and has a given length."""
    assert str(s).isalpha(), message
    assert len(s) == int(length), message


def assert_a_max(s, length, message=""):
    """checks if s consists of only alphabetical characters, and has a given maximum length."""
    assert str(s).isalpha() or s == "", message
    assert len(s) <= int(length), message


def assert_n(s, length, message=""):
    """checks if s is numeric and has a given length."""
    assert int(s), message
    assert len(s) == int(length), message


def assert_n_max(s, length, message=""):
    """checks if s is numeric and has a given length."""
    assert int(s), message
    assert len(s) <= int(length), message


def assert_an(s, length, message=""):
    """checks if s is alphanumeric and has a given length."""
    assert is_edifact_alphanum(s), message
    assert len(s) == int(length), message


def assert_an_max(s, length, message=""):
    """checks if s is alphanumeric and has a given length."""
    assert is_edifact_alphanum(s), message
    assert len(s) <= int(length), message


def assert_format(s, fmt_str, message=""):
    assert re.match(fmt_str, s), message
