parse_xml_response_responses_valid = [
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
]

parse_xml_response_responses_invalid = [
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
    "testing"
]

# Map
test_params = {
    "parse_xml_response": {
        "params": {
            "valid": parse_xml_response_responses_valid,
            "invalid": parse_xml_response_responses_invalid
        }
    }
}
