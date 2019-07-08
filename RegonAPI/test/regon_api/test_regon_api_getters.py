import pytest

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables
# Raised Exceptions
from RegonAPI.exceptions import ApiCodeTranslationError

# Tested functions

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True


# -------------------------------------------------
# get_last_code - Method
# -------------------------------------------------
def test_get_last_code_method__valid_call(api_mock):
    api_mock.service.GetValue.return_value = '4'
    code, msg = api_mock.get_last_code()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(
        pNazwaParametru='KomunikatKod')
    assert code == '4'
    assert isinstance(msg, str) or isinstance(msg, dict)


def test_get_last_code_method__invalid_call(api_mock):
    api_mock.service.GetValue.reset_mock()
    try:
        api_mock.service.GetValue.return_value = 'testing'
        code, msg = api_mock.get_last_code()
        assert False
    except ApiCodeTranslationError as e:
        assert True
        api_mock.service.GetValue.assert_called_once()
        api_mock.service.GetValue.assert_called_with(
            pNazwaParametru='KomunikatKod')


# -------------------------------------------------
# get_data_status - Method
# -------------------------------------------------
def test_get_data_status_method__valid_call(api_mock):
    api_mock.service.GetValue.return_value = '2000-10-10'
    response = api_mock.get_data_status()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(
        pNazwaParametru='StanDanych')
    assert isinstance(response, str)
    assert response == '2000-10-10'


# -------------------------------------------------
# get_service_status - Method
# -------------------------------------------------
def test_get_service_status_method__valid_call(api_mock):
    api_mock.service.GetValue.return_value = '1'
    code, msg = api_mock.get_service_status()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(
        pNazwaParametru='StatusUslugi')
    assert code == '1'
    assert isinstance(msg, str) or isinstance(msg, dict)


def test_get_service_status_method__invalid_call(api_mock):
    api_mock.service.GetValue.reset_mock()
    try:
        api_mock.service.GetValue.return_value = 'testing'
        code, msg = api_mock.get_service_status()
        assert False
    except ApiCodeTranslationError as e:
        assert True
        api_mock.service.GetValue.assert_called_once()
        api_mock.service.GetValue.assert_called_with(
            pNazwaParametru='StatusUslugi')


# -------------------------------------------------
# get_operations - Method
# -------------------------------------------------
def test_get_operations_method__valid_calls(api_mock):
    api_mock.service._operations = {"a": 1, "b": 2, "c": 3}
    operations = api_mock.get_operations()
    assert operations == ["a", "b", "c"]

    api_mock.service._operations = {}
    operations = api_mock.get_operations()
    assert operations == []


def test_get_operations_method__invalid_call(api_mock):
    api_mock.service._operations = None
    try:
        operations = api_mock.get_operations()
        assert False
    except AttributeError:
        assert True
