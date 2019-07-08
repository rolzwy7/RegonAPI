import pytest

# Testing commons

# Testing variables
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions

# Tested functions
from RegonAPI.validators import is_valid_regon14

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True


def test_is_valid_regon14_function__valid_call():
    assert is_valid_regon14(REGON14)


def test_is_valid_regon14_function__invalid_call():
    assert not is_valid_regon14("12345678512349")  # invalid regon14
    assert not is_valid_regon14("123")
    assert not is_valid_regon14(123)
