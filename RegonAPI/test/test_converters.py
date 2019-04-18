import pytest

# Testing commons

# Testing variables
from RegonAPI.testing import REGON8
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON13
from RegonAPI.testing import REGON14

# Raised Exceptions
from RegonAPI.exceptions import RegonConvertionError

# Tested functions
from RegonAPI.converters import regon8_to_9
from RegonAPI.converters import regon13_to_14


# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_converters__test_prerequisites():
    assert REGON8 is not None
    assert REGON9 is not None


# -------------------------------------------------
# regon8_to_9 - Function
# -------------------------------------------------
def test_regon8_to_9_function__valid_call():
    """ Tests if convertion is working correctly """
    assert regon8_to_9(REGON8) == REGON9


def test_regon8_to_9_function__invalid_calls():
    """ Tests if invalid data raises exception """
    invalid_params = [123, "testing", None, {}, [], ()]
    for _ in invalid_params:
        try:
            regon8_to_9(_)
            assert False
        except RegonConvertionError as e:
            assert True


# -------------------------------------------------
# regon13_to_14 - Function
# -------------------------------------------------
def test_regon13_to_14_function__valid_call():
    """ Tests if convertion is working correctly """
    assert regon13_to_14(REGON13) == REGON14


def test_regon13_to_14_function__valid_calls():
    """ Tests if invalid data raises exception """
    invalid_params = [123, "testing", None, {}, [], ()]
    for _ in invalid_params:
        try:
            regon13_to_14(_)
            assert False
        except RegonConvertionError as e:
            assert True
