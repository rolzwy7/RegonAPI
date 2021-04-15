# Test API key
API_KEY_TEST_ENV = "abcde12345abcde12345"

# Warnings
WARNINGS = {
    "WARN_IS_NOT_PRODUCTION": {
        "eng": """
        \n\r\tYou are using TEST environment.
        \r\tSet `is_production=True` while constructing
        \r\t`RegonAPI` instance to switch to production environment.

        \r\tUsing test API key: '{API_KEY_TEST_ENV}'
        \r\tKey provided to `authenticate` method will be overridden.\n
        """.format(
            API_KEY_TEST_ENV=API_KEY_TEST_ENV
        ),
        "pl": """
        \n\r\tUżywasz środowiska TESTOWEGO.
        \r\tUstaw `is_production=True` podczas konstrukcji
        \r\tinstancji klasy `RegonAPI` aby przejść do środowiska produkcyjnego.

        \r\tUżywany jest klucz testowy: '{API_KEY_TEST_ENV}'
        \r\tKlucz przekazany do metody `authenticate` zostanie nadpisany.\n
        """.format(
            API_KEY_TEST_ENV=API_KEY_TEST_ENV
        ),
    }
}
