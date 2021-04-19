from unittest import mock
import pytest

from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiCodeTranslationError
from RegonAPI.exceptions import ApiInvalidBIRVersionProvided
from RegonAPI.exceptions import ApiAuthenticationError
from RegonAPI.settings import BIR_VERSIONS

testing = {"SID": "3xg5b1m7nuoeye55h667", "KEY": "abcde12345abcde12345"}


@pytest.fixture
@mock.patch("RegonAPI.regon_api.Client", autospec=True)
def api_mock(mockClient):
    """ Creates api object with mocked client """

    def fin():
        pass

    api = RegonAPI()
    return api


@pytest.mark.first
def test_regon_api_Prerequisites():
    assert True


def test_get_last_code_CorrectResponse_ReturnTypeCorrect(api_mock):
    api_mock.service.GetValue.return_value = "4"
    code, msg = api_mock.get_last_code()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(pNazwaParametru="KomunikatKod")
    assert code == "4"
    assert isinstance(msg, str) or isinstance(msg, dict)


def test_get_last_IncorrectResponse_ExceptionRaised(api_mock):
    api_mock.service.GetValue.reset_mock()
    try:
        api_mock.service.GetValue.return_value = "testing"
        code, msg = api_mock.get_last_code()
        assert False
    except ApiCodeTranslationError as e:
        assert True
        api_mock.service.GetValue.assert_called_once()
        api_mock.service.GetValue.assert_called_with(pNazwaParametru="KomunikatKod")
    except Exception:
        assert False


def test_get_data_status_CorrectResponse_ReturnTypeCorrect(api_mock):
    api_mock.service.GetValue.return_value = "2000-10-10"
    response = api_mock.get_data_status()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(pNazwaParametru="StanDanych")
    assert isinstance(response, str)
    assert response == "2000-10-10"


def test_get_service_status_CorrectResponse_ReturnTypeCorrect(api_mock):
    api_mock.service.GetValue.return_value = "1"
    code, msg = api_mock.get_service_status()
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(pNazwaParametru="StatusUslugi")
    assert code == "1"
    assert isinstance(msg, str) or isinstance(msg, dict)


def test_get_service_status_IncorrectResponse_ExceptionRaised(api_mock):
    api_mock.service.GetValue.reset_mock()
    try:
        api_mock.service.GetValue.return_value = "testing"
        code, msg = api_mock.get_service_status()
        assert False
    except ApiCodeTranslationError as e:
        assert True
        api_mock.service.GetValue.assert_called_once()
        api_mock.service.GetValue.assert_called_with(pNazwaParametru="StatusUslugi")


def test_get_operations_OwnOperations_NoProblemsExpected(api_mock):
    api_mock.service._operations = {"a": 1, "b": 2, "c": 3}
    operations = api_mock.get_operations()
    assert operations == ["a", "b", "c"]

    api_mock.service._operations = {}
    operations = api_mock.get_operations()
    assert operations == []


def test_get_operations_NoOperatoions_ExceptionRaised(api_mock):
    api_mock.service._operations = None
    try:
        operations = api_mock.get_operations()
        assert False
    except AttributeError:
        assert True
    except Exception:
        assert False


@mock.patch("RegonAPI.regon_api.Client")
@mock.patch("RegonAPI.regon_api.Session")
@mock.patch("RegonAPI.regon_api.RegonAPI._check_session")
@mock.patch("RegonAPI.regon_api.RegonAPI._create_service")
def test_regon_api_auth_success(
    mocked_create_service, mocked_check_session, mocked_Session, mocked_Client, api_mock
):
    api_mock.service.Zaloguj.return_value = testing["SID"]
    mocked_check_session.return_value = True

    try:
        returned = api_mock.authenticate(testing["KEY"], verify=True)
        assert True
    except ApiAuthenticationError as e:
        assert False

    api_mock.service.Zaloguj.assert_called_once()
    api_mock.service.Zaloguj.assert_called_with(testing["KEY"])

    mocked_Session.assert_called_once()
    mocked_Client.assert_called_once()
    mocked_create_service.assert_called_once()

    assert api_mock.key == testing["KEY"]
    assert api_mock.sid == testing["SID"]
    assert returned == testing["SID"]


@mock.patch("RegonAPI.regon_api.Client")
@mock.patch("RegonAPI.regon_api.Session")
@mock.patch("RegonAPI.regon_api.RegonAPI._check_session")
@mock.patch("RegonAPI.regon_api.RegonAPI._create_service")
def test_regon_api_auth_failure(
    mocked_create_service, mocked_check_session, mocked_Client, mocked_Session, api_mock
):
    api_mock.service.Zaloguj.return_value = "testing"
    mocked_check_session.return_value = False
    try:
        api_mock.authenticate(testing["KEY"], verify=True)
        assert False
    except ApiAuthenticationError as e:
        assert True


def test_CorrectInit_NoProblemsExpected(api_mock):
    api_mock.service.GetValue.return_value = "2000-10-10"
    try:
        str_ = str(api_mock)
        assert True
    except Exception as e:
        assert False
    assert isinstance(str_, str)
    assert str_ != ""
    api_mock.service.GetValue.assert_called_once()
    api_mock.service.GetValue.assert_called_with(pNazwaParametru="StanDanych")


def test_CorrectParamsProvided_NoProblemsExpected(api_mock):
    # attr service_namespace
    assert isinstance(api_mock.service_namespace, str)
    # attr bir_version
    assert isinstance(api_mock.bir_version, str)
    assert api_mock.bir_version in BIR_VERSIONS
    # attr wsdl
    assert isinstance(api_mock.wsdl, str)
    # attr service_url
    assert isinstance(api_mock.service_url, str)

    assert api_mock.service is not None
    assert api_mock.key is None
    assert api_mock.sid is None

    api_mock.client.create_service.assert_called_once()
    api_mock.client.create_service.assert_called_once_with(
        api_mock.service_namespace, api_mock.service_url
    )


def test_IncorrectBirVersionProvided_ExceptionRaised():
    try:
        RegonAPI(bir_version="testing")
        assert False
    except ApiInvalidBIRVersionProvided as e:
        assert True
    except Exception as e:
        assert False
