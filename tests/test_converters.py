import pytest

from RegonAPI.exceptions import RegonConvertionError
from RegonAPI.converters import regon13_to_14
from RegonAPI.converters import regon8_to_9

testing = {
    "REGON13": "1234567851234",
    "REGON14": "12345678512347",
    "REGON8": "49270733",
    "REGON9": "492707333",
}


@pytest.mark.first
def test_converters_Prerequisites():
    assert testing["REGON8"] is not None
    assert testing["REGON9"] is not None
    assert testing["REGON13"] is not None
    assert testing["REGON14"] is not None


def test_CorrectRegon8Param_CorrectConversion():
    assert regon13_to_14(regon13=testing["REGON13"]) == testing["REGON14"]


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


def test_CorrectRegon8Param_CorrectConversion():
    """ Tests if convertion is working correctly """
    assert regon8_to_9(regon8=testing["REGON8"]) == testing["REGON9"]


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
