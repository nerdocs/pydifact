import pytest

from pydifact.utils import syntax_version_from_directory, directory_from_syntax_version


def test_edifact_syntax_version_d87a():
    assert syntax_version_from_directory("D87A") == 1


def test_edifact_syntax_version_d88b():
    assert syntax_version_from_directory("D88B") == 1


def test_edifact_syntax_version_d89a_earliest_version_2():
    assert syntax_version_from_directory("D89A") == 2


def test_edifact_syntax_version_d92b():
    assert syntax_version_from_directory("D92B") == 2


def test_edifact_syntax_version_d93a():
    assert syntax_version_from_directory("D93A") == 3


def test_edifact_syntax_version_d99b():
    assert syntax_version_from_directory("D99B") == 3


def test_edifact_syntax_version_d00a():
    assert syntax_version_from_directory("D00A") == 4


def test_edifact_syntax_version_d24b():
    assert syntax_version_from_directory("D24B") == 4


def test_edifact_syntax_version_valid_lowercase():
    assert syntax_version_from_directory("d00a") == 4


def test_edifact_syntax_version_invalid_year():
    with pytest.raises(ValueError, match="Unknown EDIFACT directory year"):
        syntax_version_from_directory("D25A")


def test_edifact_syntax_version_invalid_chars():
    with pytest.raises(ValueError, match="Invalid EDIFACT directory format"):
        syntax_version_from_directory("D25X")
    with pytest.raises(ValueError, match="Invalid EDIFACT directory format"):
        syntax_version_from_directory("S25A")


def test_edifact_syntax_directory_version_1():
    assert directory_from_syntax_version(1) == "D88"


def test_edifact_syntax_directory_version_2():
    assert directory_from_syntax_version(2) == "D92A"


def test_edifact_syntax_directory_version_3():
    assert directory_from_syntax_version(3) == "D99B"


def test_edifact_syntax_directory_version_4():
    assert directory_from_syntax_version(4) == "D24A"


def test_edifact_syntax_directory_invalid_zero():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        directory_from_syntax_version(0)  # noqa


def test_edifact_syntax_directory_invalid_version():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        directory_from_syntax_version(5)  # noqa


def test_edifact_syntax_directory_negative_version():
    with pytest.raises(ValueError, match="Unknown EDIFACT syntax version"):
        directory_from_syntax_version(-1)  # noqa


def test_edifact_syntax_directory_handles_integer_type():
    assert directory_from_syntax_version(1) == "D88"
    assert directory_from_syntax_version(2) == "D92A"
    assert directory_from_syntax_version(3) == "D99B"
    assert directory_from_syntax_version(4) == "D24A"
