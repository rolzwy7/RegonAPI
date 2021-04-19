import pytest

from RegonAPI.validators import _re_is_digit_string
from RegonAPI.validators import is_valid_regon8
from RegonAPI.validators import is_valid_regon9
from RegonAPI.validators import is_valid_regon13
from RegonAPI.validators import is_valid_regon14
from RegonAPI.validators import is_valid_date

testing = {"REGON9": "492707333", "REGON14": "12345678512347"}


@pytest.fixture
def valid_dates():
    return ["2021-04-16", "2020-01-01", "2021-1-1", "2021-4-16"]


@pytest.fixture
def invalid_dates():
    return [
        None,
        1234,
        False,
        True,
        ("2021-04-16", "2020-01-01"),
        ["2021-04-16", "2020-01-01"],
        12.45,
        2021,
        "20011-111-444",
        "01-01-02",
    ]


@pytest.mark.first
def test_validators_Prerequisites():
    assert True


def test_is_valid_regon8_function__valid_call():
    assert is_valid_regon8("12345678")


def test_is_valid_regon8_function__invalid_calls():
    assert not is_valid_regon8("123")
    assert not is_valid_regon8(123)


def test_is_valid_regon9_function__valid_call():
    assert is_valid_regon9(testing["REGON9"])


def test_is_valid_regon9_function__invalid_calls():
    assert not is_valid_regon9("492707339")  # invalid regon9
    assert not is_valid_regon9("123")
    assert not is_valid_regon9(123)


def test_is_valid_regon13_function__valid_call():
    assert is_valid_regon13("1234567891234")


def test_is_valid_regon13_function__invalid_calls():
    assert not is_valid_regon13("123")
    assert not is_valid_regon13(123)


def test_is_valid_regon14_function__valid_call():
    assert is_valid_regon14(testing["REGON14"])


def test_is_valid_regon14_function__invalid_call():
    assert not is_valid_regon14("12345678512349")  # invalid regon14
    assert not is_valid_regon14("123")
    assert not is_valid_regon14(123)


def test_re_is_digit_string_function__valid_call():
    assert _re_is_digit_string("12345", 5)


def test_re_is_digit_string_function__invalid_calls():
    assert not _re_is_digit_string("12345", 15)
    assert not _re_is_digit_string("123abc", 3)
    assert not _re_is_digit_string("abc123", 3)
    assert not _re_is_digit_string("abc123def", 3)
    assert not _re_is_digit_string("abc", 3)
    assert not _re_is_digit_string(12345, 5)
    try:
        _re_is_digit_string("12345", "5")
        assert False
    except TypeError as e:
        assert True
    try:
        _re_is_digit_string("12345", -5)
        assert False
    except Exception as e:
        assert True


def test_is_date_valid(valid_dates):
    for date in valid_dates:
        assert is_valid_date(date) is True


def test_is_date_invalid(invalid_dates):
    for date in invalid_dates:
        assert is_valid_date(date) is False
