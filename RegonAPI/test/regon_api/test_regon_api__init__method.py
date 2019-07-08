# Last revision: 08.07.2019

import pytest

# Testing commons
from RegonAPI.test.common import api_mock

# Testing variables
from RegonAPI.settings import BIR_VERSIONS

# Raised Exceptions

# Tested functions

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_Prerequisites():
    assert True


def test_CorrectParamsProvided_NoProblemsExpected(api_mock):
    # attr service_namespace
    assert isinstance(api_mock.service_namespace, str)
    # attr bir_version
    assert isinstance(api_mock.bir_version, str)
    assert(api_mock.bir_version in BIR_VERSIONS)
    # attr wsdl
    assert isinstance(api_mock.wsdl, str)
    # attr service_url
    assert isinstance(api_mock.service_url, str)

    assert api_mock.service is not None
    assert api_mock.key is None
    assert api_mock.sid is None

    api_mock.client.create_service.assert_called_once()
    api_mock.client.create_service.assert_called_once_with(
        api_mock.service_namespace,
        api_mock.service_url
    )
