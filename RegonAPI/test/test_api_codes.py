import pytest

# Testing commons

# Testing variables
from RegonAPI.settings import available_languages
from RegonAPI.api_codes_json import API_CODES

# Raised Exceptions
from RegonAPI.exceptions import ApiCodeTranslationError

# Tested functions
from RegonAPI.api_codes import t


# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_api_codes__test_prerequisites():
    assert API_CODES is not None
    assert available_languages is not None


# -------------------------------------------------
# t - Function
# -------------------------------------------------
def test_t_function__valid_calls():
    """ Tests function against its own map """
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


def test_t_function__valid_call():
    """ Tests single correct call """
    try:
        t("GetValue", "4")
        assert True
    except Exception:
        assert False


def test_t_function__invalid_language():
    """ Tests single invalid call (invalid language)"""
    try:
        t("GetValue", "4", force_lang="testing")
        assert False
    except ApiCodeTranslationError:
        assert True


def test_t_function__invalid_code():
    """ Tests single invalid call (invalid code parameter)"""
    try:
        t("GetValue", "testing")
        assert False
    except ApiCodeTranslationError:
        assert True


def test_t_function__invalid_method_and_code():
    """ Tests single invalid call (invalid method and code parameter)"""
    try:
        t("testing", "testing")
        assert False
    except ApiCodeTranslationError:
        assert True
