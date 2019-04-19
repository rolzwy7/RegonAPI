from unittest import mock

import pytest

import RegonAPI.testing as testing

import RegonAPI


@pytest.fixture
@mock.patch('RegonAPI.regon_api.Client', autospec=True)
def api_mock(mockClient):
    """ Creates api object with mocked client """
    def fin():
        pass
    api = RegonAPI.RegonAPI(testing.WSDL, testing.URL)
    return api
