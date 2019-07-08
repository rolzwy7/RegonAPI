import pytest

# Testing commons

# Raised Exceptions
from RegonAPI.exceptions import RegonConvertionError

# Tested functions
from RegonAPI.converters import regon13_to_14

# Testing variables
REGON13 = '1234567851234'
REGON14 = '12345678512347'

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert REGON13 is not None
    assert REGON14 is not None


def test_CorrectRegon8Param_CorrectConversion():
    assert regon13_to_14(regon13=REGON13) == REGON14


def test_IncorrectRegon13Param_ExceptionRaised():
    try:
        regon13_to_14(regon13="testing")
        assert False
    except RegonConvertionError:
        assert True
    except Exception:
        assert False


def test_IncorrectParamType_ExceptionRaised():
    try:
        regon13_to_14(regon13=0)
        assert False
    except RegonConvertionError:
        assert True
    except Exception:
        assert False
