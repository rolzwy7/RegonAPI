# Last revision: 08.07.2019

from unittest import mock
import pytest

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables
from RegonAPI.testing.operations import test_params
from RegonAPI.testing import REGON9
from RegonAPI.testing import REGON14

# Raised Exceptions
from RegonAPI.exceptions import ApiUnknownReportNameError

# Tested functions


# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert api_mock is not None
    assert test_params is not None
    assert REGON9 is not None
    assert REGON14 is not None


@mock.patch('RegonAPI.operations.parse_xml_response')
def test_dataDownloadFullReport_method__valid_calls(
    mocked_parse_xml_response,
    api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    calls_made = len(api_mock.reports) * 2

    for _ in api_mock.reports:
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
