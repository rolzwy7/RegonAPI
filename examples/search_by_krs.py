from RegonAPI import RegonAPI
from pprint import pprint

API_KEY = "abcde12345abcde12345"


api = RegonAPI(bir_version="bir1")
# api = RegonAPI(bir_version="bir1.1")

api.authenticate(key=API_KEY)

print("Provide valid KRS number (for example 0000006865): ", end="")
user_krs = input()
user_krs = "0000006865" if not user_krs else user_krs

res = api.searchData(krs=user_krs)

pprint(res)
