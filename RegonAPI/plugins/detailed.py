def parse_make_response_detailed(data):
    ret = {
        "info": {
            "queries": len(data)
        },
        "data": data
    }
    return ret
