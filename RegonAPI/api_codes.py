"""
    Translation of API codes to available languages
"""

import json

from . import settings
from .settings import API_CODES
from .exceptions import ApiCodeTranslationError


def t(method, code, force_lang=None):
    """Translates api code response to message

    Parameters
    ----------
    method : str
        Regon API operation (ex. GetValue)
    code : str
        API code response (ex. '1', '2', ...)
    force_lang: str
        forces function to translate to provided language despite settings

    Returns
    -------
    str
        if settings.lang is not "all".
        Translated message.
    dict
        if settings.lang is "all".
        Translated message in all available languages.

    Raises
    ------
    ApiCodeTranslationError
        if translation couldn't be performed
    """
    lang = settings.lang if force_lang is None else force_lang
    # Get by method
    msg = API_CODES.get(method, None)
    if msg is None:
        raise ApiCodeTranslationError("invalid method: %s" % method)
    # Get by code
    msg = msg.get(code, None)
    if msg is None:
        raise ApiCodeTranslationError("invalid code: %s" % code)

    if lang == "all":
        return msg

    msg = msg.get(lang, None)
    if msg is None:
        raise ApiCodeTranslationError("%s->%s for lang: '%s'" % (method, code, lang))

    return msg
