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


def test_CorrectInit_NoProblemsExpected(api_mock):
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
