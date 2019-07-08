from RegonAPI import RegonAPI
from pprint import pprint

API_KEY = "abcde12345abcde12345"

api = RegonAPI(bir_version="bir1.1")
api.authenticate(key=API_KEY)
pprint(api.get_operations())

print("Data status:", api.get_data_status())

search_result = api.searchData(krs="0000006865")
pprint(search_result)
regon = search_result[0]["Regon"]


search_result = api.dataDownloadFullReport(
    regon,
    "BIR11OsPrawna"
)
pprint(search_result)
