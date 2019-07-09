from RegonAPI import RegonAPI
from pprint import pprint

API_KEY = "abcde12345abcde12345"
CD_PROJEKT_REGON9 = "492707333"

# BIR version 1
print("-"*16, "BIR Version 1", "-"*16)
api = RegonAPI(bir_version="bir1")
api.authenticate(key=API_KEY)
# getting report for juridical person
# All report names for different entities can be found here: https://github.com/rolzwy7/RegonAPI
res = api.dataDownloadFullReport(CD_PROJEKT_REGON9, "PublDaneRaportPrawna")
pprint(res)

# BIR version 1.1
print("-"*16, "BIR Version 1.1", "-"*16)
api = RegonAPI(bir_version="bir1.1")
api.authenticate(key=API_KEY)
# getting report for juridical person
res = api.dataDownloadFullReport(CD_PROJEKT_REGON9, "BIR11OsPrawna")
pprint(res)
