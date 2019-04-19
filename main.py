WSDL = "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd"
SERVICE_URL = "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc"
API_KEY = "abcde12345abcde12345"

from RegonAPI import RegonAPI
api = RegonAPI(wsdl=WSDL, service_url=SERVICE_URL)
api.authenticate(key=API_KEY)
from pprint import pprint
pprint(api.searchData(krs="0000006865"))

print("[+] done")
