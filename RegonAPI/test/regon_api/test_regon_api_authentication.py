from unittest import mock
import pytest

import RegonAPI

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables
import RegonAPI.testing as testing

# Raised Exceptions
from RegonAPI import exceptions

# Tested functions

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True

# -------------------------------------------------
# authenticate - Method
# -------------------------------------------------
@mock.patch('RegonAPI.regon_api.Client')
@mock.patch('RegonAPI.regon_api.Session')
@mock.patch('RegonAPI.regon_api.RegonAPI._check_session')
@mock.patch('RegonAPI.regon_api.RegonAPI._create_service')
def test_regon_api_auth_success(
    mocked_create_service, mocked_check_session,
    mocked_Session, mocked_Client, api_mock
):
    api_mock.service.Zaloguj.return_value = testing.SID
    mocked_check_session.return_value = True

    try:
        returned = api_mock.authenticate(testing.KEY, verify=True)
        assert True
    except exceptions.ApiAuthenticationError as e:
        assert False

    api_mock.service.Zaloguj.assert_called_once()
    api_mock.service.Zaloguj.assert_called_with(testing.KEY)

    mocked_Session.assert_called_once()
    mocked_Client.assert_called_once()
    mocked_create_service.assert_called_once()

    assert api_mock.key == testing.KEY
    assert api_mock.sid == testing.SID
    assert returned == testing.SID


@mock.patch('RegonAPI.regon_api.Client')
@mock.patch('RegonAPI.regon_api.Session')
@mock.patch('RegonAPI.regon_api.RegonAPI._check_session')
@mock.patch('RegonAPI.regon_api.RegonAPI._create_service')
def test_regon_api_auth_failure(
    mocked_create_service, mocked_check_session, mocked_Client,
    mocked_Session, api_mock
):
    api_mock.service.Zaloguj.return_value = 'testing'
    mocked_check_session.return_value = False
    try:
        api_mock.authenticate(testing.KEY, verify=True)
        assert False
    except exceptions.ApiAuthenticationError as e:
        assert True
