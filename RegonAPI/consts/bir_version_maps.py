BIR_SETTINGS = {
    "bir1": {  # BIR1
        "TEST": {
            "SERVICE_URL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd",
        },
        "PROD": {
            "SERVICE_URL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            # Yes, it's the same WSDL address for test and production in version 1.0
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd",
        },
    },
    "bir1.1": {  # BIR1.1
        "TEST": {
            "SERVICE_URL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl",
        },
        "PROD": {
            "SERVICE_URL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            # Sneaky correction in version 1.1
            "WSDL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-prod.wsdl",
        },
    },
    "bir1.2": {  # BIR1.2
        "TEST": {
            "SERVICE_URL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            "WSDL": "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl",
        },
        "PROD": {
            "SERVICE_URL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc",
            # No correction in version 1.1
            "WSDL": "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-prod.wsdl",
        },
    },
}

BIR_VERSIONS = BIR_SETTINGS.keys()

OPERATIONS = {
    "alias_search_data": {"bir1": "DaneSzukaj", "bir1.1": "DaneSzukajPodmioty", "bir1.2": "DaneSzukajPodmioty"},
    "alias_data_download_full_report": {
        "bir1": "DanePobierzPelnyRaport",
        "bir1.1": "DanePobierzPelnyRaport",
        "bir1.2": "DanePobierzPelnyRaport"
    },
    "alias_data_download_full_group_report": {
        "bir1": NotImplementedError,
        "bir1.1": "DanePobierzRaportZbiorczy",
        "bir1.2": "DanePobierzRaportZbiorczy"
    },
}

# DanePobierzPelnyRaport - settings
DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES = [
    {
        "bir1": "PublDaneRaportFizycznaOsoba", 
        "bir1.1": "BIR11OsFizycznaDaneOgolne",
        "bir1.2": "BIR12OsFizycznaDaneOgolne"
    },
    {
        "bir1": "PublDaneRaportDzialalnoscFizycznejCeidg",
        "bir1.1": "BIR11OsFizycznaDzialalnoscCeidg",
        "bir1.2": "BIR12OsFizycznaDzialalnoscCeidg",
    },
    {
        "bir1": "PublDaneRaportDzialalnoscFizycznejRolnicza",
        "bir1.1": "BIR11OsFizycznaDzialalnoscRolnicza",
        "bir1.2": "BIR12OsFizycznaDzialalnoscRolnicza"
    },
    {
        "bir1": "PublDaneRaportDzialalnoscFizycznejPozostala",
        "bir1.1": "BIR11OsFizycznaDzialalnoscPozostala",
        "bir1.2": "BIR12OsFizycznaDzialalnoscPozostala"
    },
    {
        "bir1": "PublDaneRaportDzialalnoscFizycznejWKrupgn",
        "bir1.1": "BIR11OsFizycznaDzialalnoscSkreslonaDo20141108",
        "bir1.2": "BIR12OsFizycznaDzialalnoscSkreslonaDo20141108"
    },
    {
        "bir1": "PublDaneRaportDzialalnosciFizycznej",
        "bir1.1": "BIR11OsFizycznaPkd",
        "bir1.2": "BIR12OsFizycznaPkd"
    },
    {
        "bir1": "PublDaneRaportLokalneFizycznej",
        "bir1.1": "BIR11OsFizycznaListaJednLokalnych",
        "bir1.2": "BIR12OsFizycznaListaJednLokalnych"

    },
    {
        "bir1": "PublDaneRaportLokalnaFizycznej",
        "bir1.1": "BIR11JednLokalnaOsFizycznej",
        "bir1.2": "BIR12JednLokalnaOsFizycznej"
    },
    {
        "bir1": "PublDaneRaportDzialalnosciLokalnejFizycznej",
        "bir1.1": "BIR11JednLokalnaOsFizycznejPkd",
        "bir1.2": "BIR12JednLokalnaOsFizycznejPkd"
    },
    {
        "bir1": "PublDaneRaportPrawna",
        "bir1.1": "BIR11OsPrawna",
        "bir1.2": "BIR12OsPrawna"

    },
    {
        "bir1": "PublDaneRaportDzialalnosciPrawnej",
        "bir1.1": "BIR11OsPrawnaPkd", 
        "bir1.2": "BIR12OsPrawnaPkd"
    },
    {
        "bir1": "PublDaneRaportLokalnePrawnej",
        "bir1.1": "BIR11OsPrawnaListaJednLokalnych",
        "bir1.2": "BIR12OsPrawnaListaJednLokalnych"
    },
    {
        "bir1": "PublDaneRaportLokalnaPrawnej",
        "bir1.1": "BIR11JednLokalnaOsPrawnej",
        "bir1.2": "BIR12JednLokalnaOsPrawnej"
        
    },
    {
        "bir1": "PublDaneRaportDzialalnosciLokalnejPrawnej",
        "bir1.1": "BIR11JednLokalnaOsPrawnejPkd",
        "bir1.2": "BIR12JednLokalnaOsPrawnejPkd"
    },
    {
        "bir1": "PublDaneRaportWspolnicyPrawnej",
        "bir1.1": "BIR11OsPrawnaSpCywilnaWspolnicy",
        "bir1.2": "BIR12OsPrawnaSpCywilnaWspolnicy"
    },
    {
        "bir1": "PublDaneRaportTypJednostki", 
        "bir1.1": "BIR11TypPodmiotu", 
        "bir1.2": "BIR12TypPodmiotu"
    },
]

# DanePobierzRaportZbiorczy - settings
DANE_POBIERZ_RAPORT_ZBIORCZY_REPORT_NAMES = [
    {"bir1.1": "BIR11NowePodmiotyPrawneOrazDzialalnosciOsFizycznych", "bir1.2": "BIR11NowePodmiotyPrawneOrazDzialalnosciOsFizycznych"},
    {"bir1.1": "BIR11AktualizowanePodmiotyPrawneOrazDzialalnosciOsFizycznych", "bir1.2": "BIR11AktualizowanePodmiotyPrawneOrazDzialalnosciOsFizycznych"},
    {"bir1.1": "BIR11SkreslonePodmiotyPrawneOrazDzialalnosciOsFizycznych", "bir1.2": "BIR11SkreslonePodmiotyPrawneOrazDzialalnosciOsFizycznych"},
    {"bir1.1": "BIR11NoweJednostkiLokalne", "bir1.2": "BIR11NoweJednostkiLokalne"},
    {"bir1.1": "BIR11AktualizowaneJednostkiLokalne", "bir1.2": "BIR11AktualizowaneJednostkiLokalne" },
    {"bir1.1": "BIR11SkresloneJednostkiLokalne", "bir1.2": "BIR11SkresloneJednostkiLokalne"},
]

REPORTS = {
    "bir1": [x["bir1"] for x in DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES],
    "bir1.1": [x["bir1.1"] for x in DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES]
    + [x["bir1.1"] for x in DANE_POBIERZ_RAPORT_ZBIORCZY_REPORT_NAMES],
    "bir1.2": [x["bir1.2"] for x in DANE_POBIERZ_PELNY_RAPORT_REPORT_NAMES]
    + [x["bir1.2"] for x in DANE_POBIERZ_RAPORT_ZBIORCZY_REPORT_NAMES]
}
