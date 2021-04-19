"""
    Validator functions
"""

import re
import datetime

from . import converters
from . import settings


def _re_is_digit_string(str_, str_len):
    """Digit string validation

    Parameters
    ----------
    str_ : str
        Digit string to validate
    str_len : int
        Digit string expected length

    Returns
    -------
    bool
        True if valid, False otherwise

    Raises
    ------
    TypeError
        If str_len is not positive int
    """
    regex = "^[0-9]{%s}$" % str_len
    if not isinstance(str_, str):
        return False
    if not isinstance(str_len, int):
        raise TypeError("_re_is_digit_string - str_len is not int")
    if str_len < 0:
        raise Exception("_re_is_digit_string - str_len < 0")
    ret = re.match(regex, str_)
    return True if ret is not None else False


def is_valid_regon8(regon8):
    """Regon8 validation

    Parameters
    ----------
    regon8 : str
        REGON8

    Returns
    -------
    bool
        True if valid, False otherwise

    Raises
    ------
    TypeError
        If regon8 is not str type
    """
    ret = _re_is_digit_string(regon8, 8)
    return True if ret else False


def is_valid_regon9(regon9):
    """Regon9 validation

    Parameters
    ----------
    regon9 : str
        REGON9

    Returns
    -------
    bool
        True if valid, False otherwise

    Raises
    ------
    TypeError
        If REGON9 is not str type
    """
    if not _re_is_digit_string(regon9, 9):
        return False
    regon8 = regon9[:8]
    return converters.regon8_to_9(regon8) == regon9


def is_valid_regon13(regon13):
    """REGON13 validation

    Parameters
    ----------
    regon13 : str
        REGON13

    Returns
    -------
    bool
        True if valid, False otherwise

    Raises
    ------
    TypeError
        If REGON13 is not str type
    """
    ret = _re_is_digit_string(regon13, 13)
    return True if ret else False


def is_valid_regon14(regon14):
    """REGON14 validation

    Parameters
    ----------
    regon14 : str
        REGON14

    Returns
    -------
    bool
        True if valid, False otherwise

    Raises
    ------
    TypeError
        If REGON14 is not str type
    """
    if not _re_is_digit_string(regon14, 14):
        return False
    regon13 = regon14[:13]
    return converters.regon13_to_14(regon13) == regon14


def is_valid_date(date):
    """Date string format validation

    Parameters
    ----------
    date : str
        String containing date in yyyy-mm-dd format

    Returns
    -------
    bool
        True if valid, False otherwise
    """

    if not isinstance(date, str):
        return False

    try:
        datetime.datetime.strptime(date, settings.DATE_FORMAT)
    except Exception:
        return False
    else:
        return True
