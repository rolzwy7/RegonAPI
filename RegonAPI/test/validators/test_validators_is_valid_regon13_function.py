import pytest

# Testing commons

# Testing variables
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions

# Tested functions
from RegonAPI.validators import is_valid_regon13

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True


def test_is_valid_regon13_function__valid_call():
    assert is_valid_regon13("1234567891234")


def test_is_valid_regon13_function__invalid_calls():
    assert not is_valid_regon13("123")
    assert not is_valid_regon13(123)
