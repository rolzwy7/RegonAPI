searchData_valid_params = [
    {"krs": "0000006865"},
    {"regon": "492707333"},
    {"nip": "7342867148"},
    {"regons9": ["492707333"]},
    {"regons14": ["12345678512347"]},
    {"krss": ["0000006865"]},
    {"nips": ["7342867148"]},
]

searchData_invalid_params = [
    {},
    {
        "krs": 123,
        "regon": 123,
        "nip": 123,
        "regons9": "testing",
        "regons14": "testing",
        "krss": "testing",
        "nips": "testing"
    },
]

# Map
test_params = {
    "searchData": {
        "params": {
            "valid": searchData_valid_params,
            "invalid": searchData_invalid_params
        }
    }
}
