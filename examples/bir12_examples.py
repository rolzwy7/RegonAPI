from pprint import pprint

from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiAuthenticationError

# Available reports
REPORTS = [
    "BIR12OsFizycznaDaneOgolne",
    "BIR12OsFizycznaDzialalnoscCeidg",
    "BIR12OsFizycznaDzialalnoscRolnicza",
    "BIR12OsFizycznaDzialalnoscPozostala",
    "BIR12OsFizycznaDzialalnoscSkreslonaDo20141108",
    "BIR12OsFizycznaPkd",
    "BIR12OsFizycznaListaJednLokalnych",
    "BIR12JednLokalnaOsFizycznej",
    "BIR12JednLokalnaOsFizycznejPkd",
    "BIR12OsPrawna",
    "BIR12OsPrawnaPkd",
    "BIR12OsPrawnaListaJednLokalnych",
    "BIR12JednLokalnaOsPrawnej",
    "BIR12JednLokalnaOsPrawnejPkd",
    "BIR12OsPrawnaSpCywilnaWspolnicy",
    "BIR12TypPodmiotu",
]

TEST_API_KEY = "abcde12345abcde12345"
CD_PROJEKT_NIP = "7342867148"
CD_PROJEKT_KRS = "0000006865"
CD_PROJEKT_REGON9 = "492707333"

# Authentication
api = RegonAPI(
    bir_version="bir1.2", is_production=False, timeout=10, operation_timeout=10
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
