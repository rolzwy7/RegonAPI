"""
    Parsing functions
"""

from bs4 import BeautifulSoup


def parse_xml_response(response):
    """Parses XML response to Python dict

    Parameters
    ----------
    response : str
        XML string response from Regon API operation

    Returns
    -------
    dict
        XML data converted to dict.

    Raises
    ------
    TypeError
        If response is not a str
    """
    if not isinstance(response, str):
        raise TypeError("parse_xml_response - response")
    soup = BeautifulSoup(response, "xml")
    ret = []
    # Parse data
    filter_arr = ["\r\n", "\n", "\r"]
    for dane in soup("dane"):
        children = list(filter(lambda x: x not in filter_arr, dane.children))
        dict_elem = {}
        for _ in children:
            dict_elem[_.name] = _.get_text()
        ret.append(dict_elem.copy())

    return ret
