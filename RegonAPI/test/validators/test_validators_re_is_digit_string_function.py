import pytest

# Testing commons

# Testing variables
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions

# Tested functions
from RegonAPI.validators import _re_is_digit_string

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True


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
