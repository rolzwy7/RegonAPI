"""
    Test data
"""

SERVICE_DOMAIN = 'https://wyszukiwarkaregontest.stat.gov.pl'

WSDL = "{service_domain}/wsBIR/wsdl/UslugaBIRzewnPubl.xsd".format(
    service_domain=SERVICE_DOMAIN)


URL = '{service_domain}/wsBIR/UslugaBIRzewnPubl.svc'.format(
    service_domain=SERVICE_DOMAIN)

# CODES = api_codes_json.API_CODES

KEY = 'abcde12345abcde12345'  # Regon API official test key

SID = '3xg5b1m7nuoeye55h667'  # example sid

SERVICE_NAMESPACE = '{http://tempuri.org/}e3'

# Test numbers
KRS = '0000006865'

NIP = '7342867148'

REGON8 = '49270733'
REGON9 = '492707333'

REGON13 = '1234567851234'
REGON14 = '12345678512347'

# Available operations
available_operations = [
    "PobierzCaptcha",
    "SprawdzCaptcha",
    "GetValue",
    "SetValue",
    "Zaloguj",
    "Wyloguj",
    "DaneSzukaj",
    "DanePobierzPelnyRaport",
    "DaneKomunikat",
]
