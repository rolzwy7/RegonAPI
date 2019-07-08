from RegonAPI import RegonAPI
from pprint import pprint

API_KEY = "abcde12345abcde12345"

api = RegonAPI(bir_version="bir1")
api.authenticate(key=API_KEY)

print("Data status:", api.get_data_status())

search_result = api.searchData(krs="0000006865")
pprint(search_result)
pprint(api.get_operations())
