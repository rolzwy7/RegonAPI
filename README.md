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
from RegonAPI import RegonAPI
from pprint import pprint

API_KEY = "abcde12345abcde12345"
CD_PROJEKT_REGON9 = "492707333"

api = RegonAPI(bir_version="bir1") # BIR version 1
api.authenticate(key=API_KEY)
res = api.dataDownloadFullReport(CD_PROJEKT_REGON9, "PublDaneRaportPrawna")
pprint(res)
```

Result of the above code

```
[{'praw_adSiedzGmina_Nazwa': 'Praga-Północ',
  'praw_adSiedzGmina_Symbol': '088',
  'praw_adSiedzKodPocztowy': '03301',
  'praw_adSiedzKraj_Nazwa': 'POLSKA',
  'praw_adSiedzKraj_Symbol': 'PL',
  'praw_adSiedzMiejscowoscPoczty_Nazwa': 'Warszawa',
  'praw_adSiedzMiejscowoscPoczty_Symbol': '0919298',
  'praw_adSiedzMiejscowosc_Nazwa': 'Warszawa',
  'praw_adSiedzMiejscowosc_Symbol': '0919298',
  ......
  truncated
  ......
  'praw_formaFinansowania_Symbol': '1',
  'praw_formaWlasnosci_Nazwa': 'WŁASNOŚĆ PRYWATNA KRAJOWA POZOSTAŁA',
  'praw_formaWlasnosci_Symbol': '215',
  'praw_jednostekLokalnych': '0',
  'praw_nazwa': 'CD PROJEKT SPÓŁKA AKCYJNA',
  'praw_nazwaSkrocona': 'CD PROJEKT S.A.',
  'praw_nip': '7342867148',
  ......
  truncated
  ......
  'praw_podstawowaFormaPrawna_Nazwa': 'OSOBA PRAWNA',
  'praw_podstawowaFormaPrawna_Symbol': '1',
  'praw_regon14': '49270733300000',
  'praw_rodzajRejestruEwidencji_Nazwa': 'REJESTR PRZEDSIĘBIORCÓW',
  'praw_rodzajRejestruEwidencji_Symbol': '138',
  'praw_szczegolnaFormaPrawna_Nazwa': 'SPÓŁKI AKCYJNE',
  'praw_szczegolnaFormaPrawna_Symbol': '16'}]
```

### Report names
All report names used by function <i>dataDownloadFullReport</i> are listed <a href="https://github.com/rolzwy7/RegonAPI/wiki/Report-names">here</a> or in API documentation.

### API documentation
- [BIR Version 1 Documentation](https://api.stat.gov.pl/Content/files/regon/regon_-_instrukcja_techniczna_bir1_dla_podmiotow_komercyjnych_v019.zip)
- [BIR Version 1.1 Documentation](https://api.stat.gov.pl/Content/files/regon/GUS-Regon-UslugaBIR11-dokumentacja_v1.02.zip)

### Tests
All tests can be performed by executing this command
```
python -m pytest tests
```

<img src="http://bit.ly/2xlhl2x">
