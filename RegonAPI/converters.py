"""
    Converters of codes
"""

from string import digits

from .exceptions import RegonConvertionError
from . import validators


REGON9_WEIGHTS = [8, 9, 2, 3, 4, 5, 6, 7]
REGON14_WEIGHTS = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]


def regon8_to_9(regon8):
    """Convert REGON8 to REGON9

    Parameters
    ----------
    regon8 : str
        REGON8

    Returns
    -------
    str
        REGON9

    Raises
    ------
    RegonConvertionError
        If regon8 is not valid
    """
    if not validators.is_valid_regon8(regon8):
        raise RegonConvertionError(regon8)
    a, b = list(regon8), REGON9_WEIGHTS
    a = list(map(lambda x: int(x), a))
    last_digit = sum(list(map(lambda x: x[0] * x[1], zip(a, b)))) % 11
    regon9 = "{regon8}{last_digit}".format(regon8=regon8, last_digit=last_digit)
    return regon9


def regon13_to_14(regon13):
    """Convert REGON13 to REGON14

    Parameters
    ----------
    regon13 : str
        REGON13

    Returns
    -------
    str
        REGON14

    Raises
    ------
    RegonConvertionError
        If regon13 is not valid
    """
    if not validators.is_valid_regon13(regon13):
        raise RegonConvertionError(regon13)
    a, b = list(regon13), REGON14_WEIGHTS
    a = list(map(lambda x: int(x), a))
    last_digit = sum(list(map(lambda x: x[0] * x[1], zip(a, b)))) % 11
    regon14 = "{regon13}{last_digit}".format(regon13=regon13, last_digit=last_digit)
    return regon14
