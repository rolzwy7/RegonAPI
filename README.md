<h1 align="center">
  <a>
    RegonAPI
  </a>
  <br>
</h1>

<h4 align="center">
  <img src="https://rolzwy7.github.io/cdn/flags/pl.png" alt="PL">
    &nbsp;Klient API- <a href="https://api.stat.gov.pl/Home/RegonApi">Polska Baza Internetowa REGON</a> (BIR)
  <br>
  <img src="https://rolzwy7.github.io/cdn/flags/en.png" alt="PL">
    &nbsp;API Client - <a href="https://api.stat.gov.pl/Home/RegonApi">Polish GUS REGON Database</a> (BIR)
</h4>

<p align="center">
  <a href="https://github.com/rolzwy7/RegonAPI/releases">
    <img src="https://img.shields.io/github/tag/rolzwy7/RegonAPI.svg" alt="Github Release Tag">
  </a>
  <a href="https://pypi.org/project/RegonAPI/">
    <img src="https://img.shields.io/pypi/v/RegonAPI.svg" alt="PyPi Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/rolzwy7/RegonAPI.svg" alt="License">
  </a>
  <a href="https://github.com/rolzwy7/RegonAPI/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed" alt="Closed issues">
    <img src="https://img.shields.io/github/issues-closed-raw/rolzwy7/RegonAPI.svg">
  </a>
  <a href='https://regonapi.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/regonapi/badge/?version=latest' alt='Documentation status' />
  </a>
  <a href='#travis'>
    <img src='https://img.shields.io/travis/com/rolzwy7/RegonAPI.svg' alt='Build status' />
  </a>
  <a href='#pypi_downloads'>
    <img src='https://img.shields.io/pypi/dm/RegonAPI' alt='PyPi downloads' />
  </a>
</p>

<p align="center">
  <a href="https://regonapi.readthedocs.io/en/latest/">Documentation</a> •
  <a href="https://github.com/rolzwy7/RegonAPI/wiki">Wiki</a> •
  <a href="https://github.com/rolzwy7/RegonAPI/wiki/Installation-&-Usage">Installation & Usage</a> •
  <a href="https://github.com/rolzwy7/RegonAPI/wiki/Compatibility">Compatibility</a>
</p>


### Features
- Supports **BIR v1** and **BIR v1.1**
- Searching for information about business entities by:
  - **KRS** number/s
  - **NIP** number/s
  - **REGON** number/s
- Fetching business entities reports
- API messages available in **English** and **Polish** language

### Obtaining API Key
See [Obtaining API Key](https://github.com/rolzwy7/RegonAPI/wiki/Obtaining-API-Key) wiki section

### Installation

```
pip install RegonAPI
```

### Example
All usage examples are available in [examples](https://github.com/rolzwy7/RegonAPI/tree/master/examples) directory
```python
from pprint import pprint

from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiAuthenticationError

# Available reports
REPORTS = [
    "BIR11OsFizycznaDaneOgolne",
    "BIR11OsFizycznaDzialalnoscCeidg",
    "BIR11OsFizycznaDzialalnoscRolnicza",
    "BIR11OsFizycznaDzialalnoscPozostala",
    "BIR11OsFizycznaDzialalnoscSkreslonaDo20141108",
    "BIR11OsFizycznaPkd",
    "BIR11OsFizycznaListaJednLokalnych",
    "BIR11JednLokalnaOsFizycznej",
    "BIR11JednLokalnaOsFizycznejPkd",
    "BIR11OsPrawna",
    "BIR11OsPrawnaPkd",
    "BIR11OsPrawnaListaJednLokalnych",
    "BIR11JednLokalnaOsPrawnej",
    "BIR11JednLokalnaOsPrawnejPkd",
    "BIR11OsPrawnaSpCywilnaWspolnicy",
    "BIR11TypPodmiotu",
]

TEST_API_KEY = "abcde12345abcde12345"
CD_PROJEKT_NIP = "7342867148"
CD_PROJEKT_KRS = "0000006865"
CD_PROJEKT_REGON9 = "492707333"

# Authentication
api = RegonAPI(
    bir_version="bir1.1", is_production=False, timeout=10, operation_timeout=10
)
try:
    api.authenticate(key=TEST_API_KEY)
except ApiAuthenticationError as e:
    print("[-]", e)
    exit(0)
except Exception as e:
    raise

# Search by NIP
result = api.searchData(nip=CD_PROJEKT_NIP)
pprint(result)

# Search by KRS
result = api.searchData(krs=CD_PROJEKT_KRS)
pprint(result)

# Search by REGON
result = api.searchData(regon=CD_PROJEKT_REGON9)
pprint(result)

# Get all reports by REGON
for report_name in REPORTS:
    result = api.dataDownloadFullReport(CD_PROJEKT_REGON9, report_name)
    print("\n[*] Report:\n", report_name)
    pprint(result)
```

Result of the above code

```
  ... truncated ...
[{'praw_adSiedzGmina_Nazwa': 'Praga-Północ',
  'praw_adSiedzGmina_Symbol': '088',
  'praw_adSiedzKodPocztowy': '03301',
  'praw_adSiedzKraj_Nazwa': 'POLSKA',
  'praw_adSiedzKraj_Symbol': 'PL',
  'praw_adSiedzMiejscowoscPoczty_Nazwa': 'Warszawa',
  'praw_adSiedzMiejscowoscPoczty_Symbol': '0919298',
  'praw_adSiedzMiejscowosc_Nazwa': 'Warszawa',
  'praw_adSiedzMiejscowosc_Symbol': '0919298',
  ... truncated ...
  'praw_formaFinansowania_Symbol': '1',
  'praw_formaWlasnosci_Nazwa': 'WŁASNOŚĆ PRYWATNA KRAJOWA POZOSTAŁA',
  'praw_formaWlasnosci_Symbol': '215',
  'praw_jednostekLokalnych': '0',
  'praw_nazwa': 'CD PROJEKT SPÓŁKA AKCYJNA',
  'praw_nazwaSkrocona': 'CD PROJEKT S.A.',
  'praw_nip': '7342867148',
  ... truncated ...
```

### Report names
All report names used by function <i>dataDownloadFullReport</i> are listed <a href="https://github.com/rolzwy7/RegonAPI/wiki/Report-names">here</a> or in API documentation.

### API documentation
- [BIR Version 1.1 Documentation](https://api.stat.gov.pl/Home/RegonApi)
- [BIR Version 1 Documentation](https://api.stat.gov.pl/Home/RegonApi)

### Tests
All tests can be performed by executing this command
```
python -m pytest tests
```

<img src="http://bit.ly/2xlhl2x">
