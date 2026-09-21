import pytest

from pydifact.constants import C, M
from pydifact.exceptions import ValidationError
from pydifact.syntax.common import (
    CompositeDataElement,
    DataElement,
    validate_repr,
)


class EmptyCDataElement(CompositeDataElement):
    code = "FOO"
    schema = []


class Alpha(DataElement):
    code = "0001"
    repr = "a4"
    title = "Alpha"


class Numeric(DataElement):
    code = "0002"
    repr = "n4"


class AlphaNumMax(DataElement):
    code = "0003"
    repr = "an..3"


class Composite(CompositeDataElement):
    code = "C001"
    schema = [
        (AlphaNumMax, M, "an..3"),
        (AlphaNumMax, C, "an..3"),
        (Numeric, C, "n..4"),
    ]


@pytest.mark.parametrize(
    "value, repr",
    [
        ("ABCD", "a4"),
        ("AB D", "a4"),
        ("AB", "a..4"),
        ("", "a..4"),
        ("0000", "n4"),
        ("-1234", "n4"),
        ("12.34", "n4"),
        ("12,34", "n..4"),
        ("-123", "n..4"),
        ("AB1", "an3"),
        ("AB", "an..3"),
    ],
)
def test_validate_repr_valid(value, repr):
    validate_repr(value, repr)


@pytest.mark.parametrize(
    "value, repr",
    [
        ("toolong", "an2"),
        ("toolong", "an..2"),
        ("ABC", "a4"),
        ("ABCDE", "a..4"),
        ("AB1D", "a4"),
        ("-123", "n4"),
        ("abcd", "n4"),
        ("12345", "n..4"),
        (" 123", "n4"),
        ("1.2.3", "n..5"),
        ("AB", "an3"),
        ("ABCD", "an..3"),
    ],
)
def test_validate_repr_invalid(value, repr):
    with pytest.raises(ValidationError):
        validate_repr(value, repr)


def test_validate_repr_malformed_repr():
    with pytest.raises(ValueError):
        validate_repr("x", "xyz")


def test_data_element_mandatory_empty():
    with pytest.raises(ValidationError):
        Alpha("").validate(mandatory=True)


def test_data_element_conditional_empty():
    Alpha("").validate()


def test_data_element_conditional_present_is_checked():
    with pytest.raises(ValidationError):
        Alpha("AB1D").validate()


def test_data_element_repr_override():
    Alpha("AB").validate(repr="a..4")
    with pytest.raises(ValidationError):
        Alpha("ABCD").validate(repr="a..3")


def test_data_element_leading_zeros_numeric():
    Numeric("0000").validate()


def test_data_element_unknown_code_warns():
    class Coded(DataElement):
        code = "0004"
        repr = "an1"
        codes = {"A": {"title": "A"}}

    with pytest.warns(SyntaxWarning):
        Coded("B").validate()
    Coded("A").validate()


def test_composite_mandatory_empty():
    with pytest.raises(ValidationError):
        Composite([]).validate(mandatory=True)
    with pytest.raises(ValidationError):
        Composite(["", ""]).validate(mandatory=True)
    EmptyCDataElement([]).validate()


def test_composite_per_component_mandatory():
    Composite(["abc", "", "12"]).validate()
    Composite("abc").validate()
    with pytest.raises(ValidationError):
        Composite(["", "abc"]).validate()


def test_composite_conditional_component_is_checked():
    with pytest.raises(ValidationError):
        Composite(["abc", "toolong"]).validate()
    with pytest.raises(ValidationError):
        Composite(["abc", "", "abc"]).validate()


def test_composite_too_many_components():
    with pytest.raises(ValidationError):
        Composite(["a", "b", "1", "d"]).validate()
    with pytest.raises(ValidationError):
        EmptyCDataElement(["a"]).validate()


def test_composite_conditional_absent_skips_components():
    Composite([]).validate()
    Composite([""]).validate()
