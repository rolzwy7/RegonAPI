import pytest

# Testing commons

# Raised Exceptions
from RegonAPI.exceptions import RegonConvertionError

# Tested functions
from RegonAPI.converters import regon8_to_9

# Testing variables
REGON8 = '49270733'
REGON9 = '492707333'


# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert REGON8 is not None
    assert REGON9 is not None


def test_CorrectRegon8Param_CorrectConversion():
    """ Tests if convertion is working correctly """
    assert regon8_to_9(regon8=REGON8) == REGON9


def test_IncorrectRegon8Param_ExceptionRaised():
    try:
        regon8_to_9(regon8="testing")
        assert False
    except RegonConvertionError:
        assert True
    except Exception:
        assert False


def test_IncorrectParamType_ExceptionRaised():
    try:
        regon8_to_9(regon8=0)
        assert False
    except RegonConvertionError:
        assert True
    except Exception:
        assert False
