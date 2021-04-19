import pytest

from RegonAPI.parsers import parse_xml_response


testing = {
    "parse_xml_response": {
        "params": {
            "valid": [
                """
                    <root>
                        <dane>
                            <test_param_1>val1</test_param_1>
                            <test_param_2>val2</test_param_2>
                            <test_param_3>val3</test_param_3>
                        </dane>
                        <dane>
                            <test_param_1>val4</test_param_1>
                            <test_param_2>val5</test_param_2>
                            <test_param_3>val6</test_param_3>
                        </dane>
                    </root>
                """
            ],
            "invalid": [
                "<root><dane><a>val1</a></dane></Root>",
                "<root><dane><a>val1</a></dane><root>",
                "<root><da><a>val1</a></dane></root>",
                "<dane><a>val1</a></dane>",
                "<root></root>",
                "<root><dane><b>val1</a></dane></root>",
                "<root><dane><a>val1</a><dane><root>",
                "<root><dane>a>val1</a></dane></root>",
                "",
                None,
                0,
                123,
                "testing123",
            ],
        }
    }
}


@pytest.mark.first
def test_parsers_Prerequisites():
    assert True is not None


def test_parse_xml_response__function_valid_call():
    params = testing["parse_xml_response"]["params"]
    result = parse_xml_response(params["valid"][0])
    assert result[0]["test_param_1"] == "val1"
    assert result[0]["test_param_2"] == "val2"
    assert result[0]["test_param_3"] == "val3"
    assert result[1]["test_param_1"] == "val4"
    assert result[1]["test_param_2"] == "val5"
    assert result[1]["test_param_3"] == "val6"


def test_parse_xml_response__function_invalid_calls():
    params = testing["parse_xml_response"]["params"]
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
