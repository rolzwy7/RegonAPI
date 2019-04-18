import json

from RegonAPI import settings
from RegonAPI.api_codes_json import API_CODES
from RegonAPI.exceptions import ApiCodeTranslationError


def t(method, code, force_lang=None):
    """Translates api code response to message

    Parameters
    ----------
    method : str
        Regon API operation (ex. GetValue)
    code : str
        API code response (ex. '1', '2', ...)

    Returns
    -------
    str
        if settings.lang is not "all".
        Translated message.
    dict
        if settings.lang is "all".
        Translated message in all available languages.

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
        raise ApiCodeTranslationError("%s->%s for lang: '%s'" % (
            method, code, lang))

    return msg
