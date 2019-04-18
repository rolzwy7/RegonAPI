import pytest

# Testing commons

# Testing variables
from RegonAPI.testing.parsers import test_params

# Raised Exceptions

# Tested functions
from RegonAPI.parsers import parse_xml_response

# -------------------------------------------------
# Test prerequisites
# -------------------------------------------------
@pytest.mark.first
def test_parsers__test_prerequisites():
    assert True is not None


# -------------------------------------------------
# parse_xml_response - Function
# -------------------------------------------------
def test_parse_xml_response__function_valid_call():
    params = test_params["parse_xml_response"]["params"]
    result = parse_xml_response(params["valid"][0])
    assert result[0]["test_param_1"] == "val1"
    assert result[0]["test_param_2"] == "val2"
    assert result[0]["test_param_3"] == "val3"
    assert result[1]["test_param_1"] == "val4"
    assert result[1]["test_param_2"] == "val5"
    assert result[1]["test_param_3"] == "val6"


def test_parse_xml_response__function_invalid_calls():
    params = test_params["parse_xml_response"]["params"]
    for _ in params["invalid"]:
        try:
            parse_xml_response(_)
            assert False
        except Exception as e:
            assert True


def test_parse_xml_response__function_invalid_call():
    try:
        parse_xml_response(None)
        assert False
    except TypeError:
        assert True
