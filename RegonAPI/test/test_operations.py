from unittest import mock
import pytest

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables
from RegonAPI.testing.operations import test_params
from RegonAPI.testing import REPORTS
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions
from RegonAPI.exceptions import ApiUnknownReportNameError

# Tested functions


# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_operations__test_prerequisites():
    assert api_mock is not None

    assert test_params is not None
    assert REPORTS is not None
    assert REGON9 is not None
    assert REGON14 is not None


# -------------------------------------------------
# searchData - Method
# -------------------------------------------------
@mock.patch('RegonAPI.operations.parse_xml_response')
def test_searchData_method__valid_calls(mocked_parse_xml_response, api_mock):
    mocked_parse_xml_response.return_value = "testing"

    params = test_params["searchData"]["params"]
    calls_made = len(params["valid"])

    for tc in params["valid"]:
        assert api_mock.searchData(**tc) == "testing"
    mocked_parse_xml_response.call_count == calls_made
    api_mock.service.DaneSzukaj.call_count == calls_made


@mock.patch('RegonAPI.operations.parse_xml_response')
def test_searchData_method__invalid_calls(mocked_parse_xml_response, api_mock):
    mocked_parse_xml_response.return_value = "testing"

    params = test_params["searchData"]["params"]

    for tc in params["invalid"]:
        try:
            api_mock.searchData(**tc)
        except TypeError as e:
            assert True
        except Exception as e:
            assert True


# -------------------------------------------------
# dataDownloadFullReport - Method
# -------------------------------------------------
@mock.patch('RegonAPI.operations.parse_xml_response')
def test_dataDownloadFullReport_method__valid_calls(
    mocked_parse_xml_response,
    api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    calls_made = len(REPORTS) * 2

    for _ in REPORTS:
        assert api_mock.dataDownloadFullReport(REGON9, _) == "testing"
        assert api_mock.dataDownloadFullReport(REGON14, _) == "testing"

    assert mocked_parse_xml_response.call_count == calls_made
    assert api_mock.service.DanePobierzPelnyRaport.call_count == calls_made


@mock.patch('RegonAPI.operations.parse_xml_response')
def test_dataDownloadFullReport_method__invalid_report_name(
    mocked_parse_xml_response,
    api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    try:
        api_mock.dataDownloadFullReport(REGON9, "testing")
        assert False
    except ApiUnknownReportNameError as e:
        assert True
