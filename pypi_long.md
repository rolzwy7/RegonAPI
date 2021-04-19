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

# Group reports

GROUP_REPORTS = [
    "BIR11NowePodmiotyPrawneOrazDzialalnosciOsFizycznych",
    "BIR11AktualizowanePodmiotyPrawneOrazDzialalnosciOsFizycznych",
    "BIR11SkreslonePodmiotyPrawneOrazDzialalnosciOsFizycznych",
    "BIR11NoweJednostkiLokalne",
    "BIR11AktualizowaneJednostkiLokalne",
    "BIR11SkresloneJednostkiLokalne",
]

# It's better to fetch group reports using your own API key
print("\n[!] It's better to fetch group reports using your own API key")
exit(0)

for group_report_name in GROUP_REPORTS:
    result = api.dataDownloadFullGroupReport("2021-04-16", group_report_name)
    print("\n[*] Group Report:\n", group_report_name)
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
