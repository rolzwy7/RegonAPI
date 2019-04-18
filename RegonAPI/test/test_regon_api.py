import pytest

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables

# Raised Exceptions

# Tested functions

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_regon_api__test_prerequisites():
    assert True


# -------------------------------------------------
# RegonAPI __init__
# -------------------------------------------------
def test_regon_api__init__(api_mock):
    assert isinstance(api_mock.service_namespace, str)
    assert isinstance(api_mock.wsdl, str)
    assert isinstance(api_mock.service_url, str)
    assert api_mock.service is not None
    assert api_mock.key is None
    assert api_mock.sid is None
    api_mock.client.create_service.assert_called_once()
    api_mock.client.create_service.assert_called_once_with(
        api_mock.service_namespace,
        api_mock.service_url
    )


# -------------------------------------------------
# RegonAPI __str__
# -------------------------------------------------
def test_regon_api__str__(api_mock):
    api_mock.service.GetValue.return_value = '2000-10-10'
    try:
        str_ = str(api_mock)
        assert True
    except Exception as e:
        assert False
    assert isinstance(str_, str)
    assert str_ != ''
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(
        pNazwaParametru='StanDanych')
