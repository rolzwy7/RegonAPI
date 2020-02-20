from RegonAPI import RegonAPI

api = RegonAPI(bir_version="bir1.1", is_production=False)
try:
    api.authenticate(key="")
except Exception as e:
    raise
