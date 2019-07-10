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
    <img src="https://img.shields.io/github/tag/rolzwy7/RegonAPI.svg" alt="Version">
  </a>
  <a href="https://pypi.org/project/RegonAPI/">
    <img src="https://img.shields.io/pypi/v/RegonAPI.svg" alt="Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/rolzwy7/RegonAPI.svg">
  </a>
  <a href="https://github.com/rolzwy7/RegonAPI/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-closed-raw/rolzwy7/RegonAPI.svg">
  </a>
  <a href='https://regonapi.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/regonapi/badge/?version=latest' alt='Documentation Status' />
  </a>
  <a href='https://regonapi.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://img.shields.io/travis/com/rolzwy7/RegonAPI.svg' alt='Documentation Status' />
  </a>

</p>

<p align="center">
  <a href="#documentation">Documentation</a> •
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

### Report names
All report names used by function <i>dataDownloadFullReport</i> are listed <a href="https://github.com/rolzwy7/RegonAPI/wiki/Report-names">here</a> or in API documentation.

### API documentation
- [BIR Version 1 Documentation](https://api.stat.gov.pl/Content/files/regon/regon_-_instrukcja_techniczna_bir1_dla_podmiotow_komercyjnych_v019.zip)
- [BIR Version 1.1 Documentation](https://api.stat.gov.pl/Content/files/regon/GUS-Regon-UslugaBIR11-dokumentacja_v1.02.zip)

### Tests
All tests can be performed by executing this command
```
python -m pytest -v RegonAPI\test
```
