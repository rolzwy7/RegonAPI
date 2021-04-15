API_CODES = {
    "Type": {
        "P": {
            "pl": "Typ jednostki – jednostka prawna",
            "eng": "Type of entity - juridical person",
        },
        "F": {
            "pl": "Typ jednostki – jednostka fizyczna (os. fizyczna prowadząca działalność gospodarczą)",
            "eng": "Type of entity - natural person",
        },
        "LP": {
            "pl": "Typ jednostki – jednostka lokalna jednostki prawnej",
            "eng": "Type of entity - local entity of juridical person",
        },
        "LF": {
            "pl": "Typ jednostki – jednostka lokalna jednostki fizycznej",
            "eng": "Type of entity - local entity of natural person",
        },
    },
    "SilosID": {
        "1": {
            "pl": "Miejsce prowadzenia działalności zarejestrowanej w CEIDG (tylko typy F i LF))",
            "eng": "Registered in CEIDG (only types F and LF)",
        },
        "2": {
            "pl": "Miejsce prowadzenia działalności rolniczej (tylko typy F i LF))",
            "eng": "Agricultural (only types F and LF)",
        },
        "3": {
            "pl": "Miejsce prowadzenia działalności pozostałej (tylko typy F i LF))",
            "eng": "Other activity (only types F and LF)",
        },
        "4": {
            "pl": "Miejsce prowadzenia działalności zlikwidowanej w starym systemie KRUPGN",
            "eng": "Liquidated (old KRUPGN system)",
        },
        "6": {
            "pl": "Miejsce prowadzenia działalności jednostki prawnej (tylko typy P i LP)",
            "eng": "Juridical person (only types P and LP)",
        },
    },
    "GetValue": {
        "0": {"pl": "Brak wiadomości", "eng": "No messages"},
        "1": {
            "pl": "Konieczne jest pobranie i sprawdzenie kodu Captcha (metody PobierzCaptcha i SprawdzCaptcha).",
            "eng": "It's necessary to download and check Captcha code (methods PobierzCaptcha i SprawdzCaptcha)",
        },
        "2": {
            "pl": "Do metody DaneSzukaj przekazano zbyt wiele identyfikatorów.",
            "eng": "Too much parameters passed to DaneSzukaj method",
        },
        "4": {"pl": "Nie znaleziono podmiotów.", "eng": "Can't find entity"},
        "5": {
            "pl": "Brak uprawnień do raportu.",
            "eng": "Insufficient privileges for this report",
        },
        "7": {
            "pl": "Brak sesji. Sesja wygasła lub przekazano nieprawidłową wartość nagłówka sid.",
            "eng": "Session failure. Session expired or sid header is incorrect",
        },
    },
    "ServiceStatus": {
        "0": {"pl": "Niedostępna", "eng": "Unavailable"},
        "1": {"pl": "Dostępna", "eng": "Available"},
        "2": {"pl": "Przerwa techniczna", "eng": "Maintenance"},
    },
}
