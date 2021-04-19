from unittest import mock
import pytest

from RegonAPI.exceptions import ApiUnknownReportNameError
from RegonAPI import RegonAPI

testing = {
    "REGON9": "492707333",
    "REGON14": "12345678512347",
    "test_params": {
        "searchData": {
            "params": {
                "valid": [
                    {"krs": "0000006865"},
                    {"regon": "492707333"},
                    {"nip": "7342867148"},
                    {"regons9": ["492707333"]},
                    {"regons14": ["12345678512347"]},
                    {"krss": ["0000006865"]},
                    {"nips": ["7342867148"]},
                ],
                "invalid": [
                    {},
                    {
                        "krs": 123,
                        "regon": 123,
                        "nip": 123,
                        "regons9": "testing",
                        "regons14": "testing",
                        "krss": "testing",
                        "nips": "testing",
                    },
                ],
            }
        }
    },
}


@pytest.fixture
@mock.patch("RegonAPI.regon_api.Client", autospec=True)
def api_mock(mockClient):
    """ Creates api object with mocked client """

    def fin():
        pass

    api = RegonAPI()
    return api


@pytest.mark.first
def test_operations_Prerequisites():
    assert api_mock is not None
    assert testing is not None
    assert testing["test_params"] is not None
    assert testing["REGON9"] is not None
    assert testing["REGON14"] is not None


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_dataDownloadFullReport_method__valid_calls(
    mocked_parse_xml_response, api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    calls_made = len(api_mock.reports) * 2

    for _ in api_mock.reports:
        assert api_mock.dataDownloadFullReport(testing["REGON9"], _) == "testing"
        assert api_mock.dataDownloadFullReport(testing["REGON14"], _) == "testing"

    assert mocked_parse_xml_response.call_count == calls_made
    assert api_mock.service.DanePobierzPelnyRaport.call_count == calls_made


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_dataDownloadFullReport_method__invalid_report_name(
    mocked_parse_xml_response, api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    try:
        api_mock.dataDownloadFullReport(testing["REGON9"], "testing")
        assert False
    except ApiUnknownReportNameError as e:
        assert True


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_searchData_method__valid_calls(mocked_parse_xml_response, api_mock):
    mocked_parse_xml_response.return_value = "testing"

    params = testing["test_params"]["searchData"]["params"]
    calls_made = len(params["valid"])

    for tc in params["valid"]:
        assert api_mock.searchData(**tc) == "testing"
    mocked_parse_xml_response.call_count == calls_made
    api_mock.service.DaneSzukaj.call_count == calls_made


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_searchData_method__invalid_calls(mocked_parse_xml_response, api_mock):
    mocked_parse_xml_response.return_value = "testing"

    params = testing["test_params"]["searchData"]["params"]

    for tc in params["invalid"]:
        try:
            api_mock.searchData(**tc)
        except TypeError as e:
            assert True
        except Exception as e:
            assert True


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_dataDownloadFullGroupReport_method__valid_calls(
    mocked_parse_xml_response, api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    calls_made = len(api_mock.reports)

    for report in api_mock.reports:
        assert (
            api_mock.dataDownloadFullGroupReport(
                report_date="2020-04-16", report_name=report
            )
            == "testing"
        )

    assert mocked_parse_xml_response.call_count == calls_made
    assert api_mock.service.DanePobierzRaportZbiorczy.call_count == calls_made


@mock.patch("RegonAPI.operations.parse_xml_response")
def test_dataDownloadFullGroupReport_method__invalid_report_name(
    mocked_parse_xml_response, api_mock
):
    mocked_parse_xml_response.return_value = "testing"

    with pytest.raises(ApiUnknownReportNameError):
        api_mock.dataDownloadFullGroupReport(
            report_date="2021-04-16", report_name="test"
        )
