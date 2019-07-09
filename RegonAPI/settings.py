import os
import logging

from RegonAPI.consts import API_CODES
from RegonAPI.consts import VOIVODESHIPS
from RegonAPI.consts import BIR_SETTINGS
from RegonAPI.consts import BIR_VERSIONS
from RegonAPI.consts import OPERATIONS
from RegonAPI.consts import DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES
from RegonAPI.consts import REPORTS

# Language - settings
lang = 'eng'

# Logger - settings
available_languages = ["pl", "eng"]
logging_level = logging.WARNING
logging_file_handler_level = logging.WARNING
logging_stream_handler_level = logging.WARNING
