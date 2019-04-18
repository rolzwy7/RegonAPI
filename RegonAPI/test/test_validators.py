import pytest

# Testing commons

# Testing variables
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions

# Tested functions
from RegonAPI.validators import _re_is_digit_string
from RegonAPI.validators import is_valid_regon8
from RegonAPI.validators import is_valid_regon9
from RegonAPI.validators import is_valid_regon13
from RegonAPI.validators import is_valid_regon14

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_validators__test_prerequisites():
    assert True


# -------------------------------------------------
# re_is_digit_string - Function
# -------------------------------------------------
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


# -------------------------------------------------
# is_valid_regon8 - Function
# -------------------------------------------------
def test_is_valid_regon8_function__valid_call():
    assert is_valid_regon8("12345678")


def test_is_valid_regon8_function__invalid_calls():
    assert not is_valid_regon8("123")
    assert not is_valid_regon8(123)


# -------------------------------------------------
# is_valid_regon9 - Function
# -------------------------------------------------
def test_is_valid_regon9_function__valid_call():
    assert is_valid_regon9(REGON9)


def test_is_valid_regon9_function__invalid_calls():
    assert not is_valid_regon9("492707339")  # invalid regon9
    assert not is_valid_regon9("123")
    assert not is_valid_regon9(123)


# -------------------------------------------------
# is_valid_regon13 - Function
# -------------------------------------------------
def test_is_valid_regon13_function__valid_call():
    assert is_valid_regon13("1234567891234")


def test_is_valid_regon13_function__invalid_calls():
    assert not is_valid_regon13("123")
    assert not is_valid_regon13(123)


# -------------------------------------------------
# is_valid_regon14 - Function
# -------------------------------------------------
def test_is_valid_regon14_function__valid_call():
    assert is_valid_regon14(REGON14)


def test_is_valid_regon14_function__invalid_call():
    assert not is_valid_regon14("12345678512349")  # invalid regon14
    assert not is_valid_regon14("123")
    assert not is_valid_regon14(123)
