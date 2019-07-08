import os
import logging

# BIR variables

BIR_SETTINGS = {
    "bir1": {  # BIR1
        "TEST": {
            "SERVICE_URL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd"
        },
        "PROD": {
            "SERVICE_URL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            # Yes, it's the same WSDL address for test and production.
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd"
        }
    },
    "bir1.1": {  # BIR1.1
        "TEST": {
            "SERVICE_URL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl"
        },
        "PROD": {
            "SERVICE_URL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-prod.wsdl"
        }
    }
}

BIR_VERSIONS = BIR_SETTINGS.keys()

# Language - settings
lang = 'eng'

# Logger - settings
available_languages = ["pl", "eng"]
logging_level = logging.WARNING
logging_file_handler_level = logging.WARNING
logging_stream_handler_level = logging.WARNING

OPERATIONS = {
    "alias_search_data": {
        "bir1": "DaneSzukaj",
        "bir1.1": "DaneSzukajPodmioty"
    },
    "alias_data_download_full_report": {
        "bir1": "DanePobierzPelnyRaport",
        "bir1.1": "DanePobierzPelnyRaport"
    },
    "alias_data_download_full_report": {
        "bir1": NotImplementedError,
        "bir1.1": "DanePobierzRaportZbiorczy"
    }
}

# DanePobierzPelnyRaport - settings
DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES = [
    {
     "bir1": "PublDaneRaportFizycznaOsoba",
     "bir1.1": "BIR11OsFizycznaDaneOgolne"
    },
    {
     "bir1": "PublDaneRaportDzialalnoscFizycznejCeidg",
     "bir1.1": "BIR11OsFizycznaDzialalnoscCeidg"
    },
    {
     "bir1": "PublDaneRaportDzialalnoscFizycznejRolnicza",
     "bir1.1": "BIR11OsFizycznaDzialalnoscRolnicza"
    },
    {
     "bir1": "PublDaneRaportDzialalnoscFizycznejPozostala",
     "bir1.1": "BIR11OsFizycznaDzialalnoscPozostala"
    },
    {
     "bir1": "PublDaneRaportDzialalnoscFizycznejWKrupgn",
     "bir1.1": "BIR11OsFizycznaDzialalnoscSkreslonaDo20141108"
    },
    {
     "bir1": "PublDaneRaportDzialalnosciFizycznej",
     "bir1.1": "BIR11OsFizycznaPkd"
    },
    {
     "bir1": "PublDaneRaportLokalneFizycznej",
     "bir1.1": "BIR11OsFizycznaListaJednLokalnych"
    },
    {
     "bir1": "PublDaneRaportLokalnaFizycznej",
     "bir1.1": "BIR11JednLokalnaOsFizycznej"
    },
    {
     "bir1": "PublDaneRaportDzialalnosciLokalnejFizycznej",
     "bir1.1": "BIR11JednLokalnaOsFizycznejPkd"
    },
    {
     "bir1": "PublDaneRaportPrawna",
     "bir1.1": "BIR11OsPrawna"
    },
    {
     "bir1": "PublDaneRaportDzialalnosciPrawnej",
     "bir1.1": "BIR11OsPrawnaPkd"
    },
    {
     "bir1": "PublDaneRaportLokalnePrawnej",
     "bir1.1": "BIR11OsPrawnaListaJednLokalnych"
    },
    {
     "bir1": "PublDaneRaportLokalnaPrawnej",
     "bir1.1": "BIR11JednLokalnaOsPrawnej"
    },
    {
     "bir1": "PublDaneRaportDzialalnosciLokalnejPrawnej",
     "bir1.1": "BIR11JednLokalnaOsPrawnejPkd"
    },
    {
     "bir1": "PublDaneRaportWspolnicyPrawnej",
     "bir1.1": "BIR11OsPrawnaSpCywilnaWspolnicy"
    },
    {
     "bir1": "PublDaneRaportTypJednostki",
     "bir1.1": "BIR11TypPodmiotu"
    }
]

# Since BIR 1.1 DanePobierzPelnyRaport has 16 possible reports to fetch
assert len(DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES) == 16

REPORTS = {
    "bir1": [x["bir1"] for x in DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES],
    "bir1.1": [x["bir1.1"] for x in DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES]
}


API_CODES = {
    "Type": {
        "P": {
                "pl": "Typ jednostki – jednostka prawna",
                "eng": "Type of entity - juridical person"
            },
        "F": {
                "pl": "Typ jednostki – jednostka fizyczna (os. fizyczna prowadząca działalność gospodarczą)",
                "eng": "Type of entity - natural person"
            },
        "LP": {
                "pl": "Typ jednostki – jednostka lokalna jednostki prawnej",
                "eng": "Type of entity - local entity of juridical person"
            },
        "LF": {
                "pl": "Typ jednostki – jednostka lokalna jednostki fizycznej",
                "eng": "Type of entity - local entity of natural person"
            }
    },
    "SilosID": {
        "1": {
                "pl": "Miejsce prowadzenia działalności zarejestrowanej w CEIDG (tylko typy F i LF))",
                "eng": "Registered in CEIDG (only types F and LF)"
            },
        "2": {
                "pl": "Miejsce prowadzenia działalności rolniczej (tylko typy F i LF))",
                "eng": "Agricultural (only types F and LF)"
            },
        "3": {
                "pl": "Miejsce prowadzenia działalności pozostałej (tylko typy F i LF))",
                "eng": "Other activity (only types F and LF)"
            },
        "4": {
                "pl": "Miejsce prowadzenia działalności zlikwidowanej w starym systemie KRUPGN",
                "eng": "Liquidated (old KRUPGN system)"
            },
        "6": {
                "pl": "Miejsce prowadzenia działalności jednostki prawnej (tylko typy P i LP)",
                "eng": "Juridical person (only types P and LP)"
            }
    },
    "GetValue": {
        "0": {
                "pl": "Brak wiadomości",
                "eng": "No messages"
            },
        "1": {
                "pl": "Konieczne jest pobranie i sprawdzenie kodu Captcha (metody PobierzCaptcha i SprawdzCaptcha).",
                "eng": "It's necessary to download and check Captcha code (methods PobierzCaptcha i SprawdzCaptcha)"
            },
        "2": {
                "pl": "Do metody DaneSzukaj przekazano zbyt wiele identyfikatorów.",
                "eng": "Too much parameters passed to DaneSzukaj method"
            },
        "4": {
                "pl": "Nie znaleziono podmiotów.",
                "eng": "Can't find entity"
            },
        "5": {
                "pl": "Brak uprawnień do raportu.",
                "eng": "Insufficient privileges for this report"
            },
        "7": {
                "pl": "Brak sesji. Sesja wygasła lub przekazano nieprawidłową wartość nagłówka sid.",
                "eng": "Session failure. Session expired or sid header is incorrect"
            }
    },
    "ServiceStatus": {
        "0": {
                "pl": "Niedostępna",
                "eng": "Unavailable"
        },
        "1": {
                "pl": "Dostępna",
                "eng": "Available"
        },
        "2": {
                "pl": "Przerwa techniczna",
                "eng": "Maintenance"
        }
    }
}
