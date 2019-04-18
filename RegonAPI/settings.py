import os
import logging

lang = 'eng'

available_languages = ["pl", "eng"]
logging_level = logging.WARNING
logging_file_handler_level = logging.WARNING
logging_stream_handler_level = logging.WARNING

REPORTS = [
    "PublDaneRaportFizycznaOsoba",
    "PublDaneRaportDzialalnoscFizycznejCeidg",
    "PublDaneRaportDzialalnoscFizycznejRolnicza",
    "PublDaneRaportDzialalnoscFizycznejPozostala",
    "PublDaneRaportDzialalnoscFizycznejWKrupgn",
    "PublDaneRaportLokalneFizycznej",
    "PublDaneRaportLokalnaFizycznej",
    "PublDaneRaportDzialalnosciFizycznej",
    "PublDaneRaportDzialalnosciLokalnejFizycznej",
    "PublDaneRaportPrawna",
    "PublDaneRaportDzialalnosciPrawnej",
    "PublDaneRaportLokalnePrawnej",
    "PublDaneRaportLokalnaPrawnej",
    "PublDaneRaportDzialalnosciLokalnejPrawnej",
    "PublDaneRaportWspolnicyPrawnej",
    "PublDaneRaportTypJednostki"
]
