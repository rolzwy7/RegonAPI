import pytest

from RegonAPI.exceptions import ApiCodeTranslationError
from RegonAPI.settings import available_languages
from RegonAPI.settings import API_CODES
from RegonAPI.api_codes import t


@pytest.mark.first
def test_api_codes_Prerequisites():
    assert API_CODES is not None
    assert available_languages is not None


def test_t_CorrectOwnMapProvided_NoProblemsExpected():
    for method_key, method_value in API_CODES.items():
        testing_method = method_key
        for code in method_value.keys():
            try:
                # For settings.lang
                ret = t(method_key, code)
                assert isinstance(ret, str) or isinstance(ret, dict)
                # For forced lang
                for lang in available_languages:
                    ret = t(method_key, code, force_lang=lang)
                    assert isinstance(ret, str)
                    assert True
            except Exception as e:
                assert False


def test_t_CorrectParamsProvided_NoExceptionRaised():
    try:
        t(method="GetValue", code="4")
        assert True
    except Exception:
        assert False


def test_t_IncorrectCodeParamProvided_ExceptionRaised():
    try:
        t(method="GetValue", code="testing")
        assert False
    except ApiCodeTranslationError:
        assert True
    except Exception:
        assert False


def test_t_IncorrectMethodParamProvided_ExceptionRaised():
    try:
        t(method="testing", code="4")
        assert False
    except ApiCodeTranslationError:
        assert True
    except Exception:
        assert False


def test_t_IncorrectForceLangParamProvided_ExceptionRaised():
    try:
        t(method="GetValue", code="4", force_lang="testing")
        assert False
    except ApiCodeTranslationError:
        assert True
    except Exception:
        assert False


def test_t_CorrectForceLangParamProvided_NoExceptionRaised():
    try:
        t(method="GetValue", code="4", force_lang="pl")
        assert True
    except ApiCodeTranslationError:
        assert False
