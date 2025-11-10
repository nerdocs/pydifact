import pytest

from pydifact.utils import edifact_syntax_version, edifact_syntax_directory


def test_edifact_syntax_version_d87a():
    assert edifact_syntax_version("D87A") == 1


def test_edifact_syntax_version_d88b():
    assert edifact_syntax_version("D88B") == 1


def test_edifact_syntax_version_d89a_earliest_version_2():
    assert edifact_syntax_version("D89A") == 2


def test_edifact_syntax_version_d92b():
    assert edifact_syntax_version("D92B") == 2


def test_edifact_syntax_version_d93a():
    assert edifact_syntax_version("D93A") == 3


def test_edifact_syntax_version_d99b():
    assert edifact_syntax_version("D99B") == 3


def test_edifact_syntax_version_d00a():
    assert edifact_syntax_version("D00A") == 4


def test_edifact_syntax_version_d24b():
    assert edifact_syntax_version("D24B") == 4


def test_edifact_syntax_version_valid_lowercase():
    assert edifact_syntax_version("d00a") == 4


def test_edifact_syntax_version_invalid_year():
    with pytest.raises(ValueError, match="Unknown EDIFACT directory year"):
        edifact_syntax_version("D25A")


def test_edifact_syntax_version_invalid_chars():
    with pytest.raises(ValueError, match="Invalid EDIFACT directory format"):
        edifact_syntax_version("D25X")
    with pytest.raises(ValueError, match="Invalid EDIFACT directory format"):
        edifact_syntax_version("S25A")


def test_edifact_syntax_directory_version_1():
    assert edifact_syntax_directory(1) == "D88"


def test_edifact_syntax_directory_version_2():
    assert edifact_syntax_directory(2) == "D92A"


def test_edifact_syntax_directory_version_3():
    assert edifact_syntax_directory(3) == "D99B"


def test_edifact_syntax_directory_version_4():
    assert edifact_syntax_directory(4) == "D24A"


def test_edifact_syntax_directory_invalid_zero():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        edifact_syntax_directory(0)  # noqa


def test_edifact_syntax_directory_invalid_version():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        edifact_syntax_directory(5)  # noqa


def test_edifact_syntax_directory_negative_version():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        edifact_syntax_directory(-1)  # noqa


def test_edifact_syntax_directory_handles_integer_type():
    assert edifact_syntax_directory(1) == "D88"
    assert edifact_syntax_directory(2) == "D92A"
    assert edifact_syntax_directory(3) == "D99B"
    assert edifact_syntax_directory(4) == "D24A"
