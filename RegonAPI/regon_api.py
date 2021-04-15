"""
    RegonAPI main client class
"""

import sys

if sys.version_info[0] < 3:
    print("Sorry. This module doesn't support Python2")
    sys.exit(1)

import logging

from requests import Session
from zeep.transports import Transport
from zeep import Client

from .api_codes import t
from .exceptions import ApiInvalidBIRVersionProvided, ApiAuthenticationError
from .operations import RegonAPIOperations
from .settings import (
    lang,
    BIR_VERSIONS,
    BIR_SETTINGS,
    REPORTS,
    DEV_ENV_WARNINGS,
    API_KEY_TEST_ENV,
    LOGGING_FORMAT,
)

# logger configuration
ROOT_LOGGING_LEVEL = logging.ERROR
LOCAL_LOGGING_LEVEL = logging.WARNING
logging.basicConfig(format=LOGGING_FORMAT)
logging.root.setLevel(ROOT_LOGGING_LEVEL)
logger = logging.getLogger(__name__)
logger.setLevel(LOCAL_LOGGING_LEVEL)


class RegonAPI(RegonAPIOperations):
    """Regon API client

    Parameters
    ----------
    bir_version : str
        BIR version to use
    is_production : bool
        Production if True, Test if False
    service_namespace : str
        Service namespace default: {http://tempuri.org/}e3
    timeout
        (Zeep) The timeout for loading wsdl and xsd documents.
    operation_timeout
        (Zeep) The timeout for operations (POST/GET).

    Attributes
    ----------
    wsdl : str
        Regon API WSDL (Web Services Description Language) URL
    service_url : str
        Service URL provided by RegonAPI Administrators
    client : zeep.client.Client
        zeep module Client object
    service : zeep.proxy.ServiceProxy
        zeep module ServiceProxy object. Used to perform SOAP requests
    key : str
        Regon API key
    sid : str
        session id
    """

    def __init__(
        self,
        bir_version="bir1.1",
        is_production=False,
        service_namespace="{http://tempuri.org/}e3",
        timeout=10,
        operation_timeout=10,
    ):
        # Set timeouts for zeep's Transport class instance
        self.timeout = timeout
        self.operation_timeout = operation_timeout

        # Set BIR version
        self.bir_version = bir_version.lower()
        if self.bir_version not in BIR_VERSIONS:
            raise ApiInvalidBIRVersionProvided(bir_version, BIR_VERSIONS)

        # Set BIR version reports
        self.reports = REPORTS[self.bir_version]

        # Set API environment
        api_env = "PROD" if is_production else "TEST"
        if not is_production:
            logger.warning(DEV_ENV_WARNINGS["WARN_IS_NOT_PRODUCTION"][lang])

        # Set WSDL & SERVICE_URL based on BIR version
        self.wsdl = BIR_SETTINGS[bir_version][api_env]["WSDL"]
        self.service_url = BIR_SETTINGS[bir_version][api_env]["SERVICE_URL"]

        logger.debug("wsdl=%s service_url=%s" % (self.wsdl, self.service_url))

        self.client = Client(wsdl=self.wsdl)
        self.service = None
        self.key = None
        self.sid = None
        self.is_production = is_production
        self.service_namespace = service_namespace
        self._create_service()

    def authenticate(self, key, verify=True):
        """Authenticates client

        Note
        ----
        This method additionaly sets sid (session id) header in Client's
        Session object. There is no need to set it manually.

        This method additionaly sets 'key' attribute

        This method additionaly sets 'sid' attribute

        Parameters
        ----------
        key : str
            API key
        verify : bool
            If True verifies if authentication was successfull

        Returns
        -------
        str
            sid (session id) required by API for further requests.

        Raises
        ------
        ApiAuthenticationError
            If authentication was a failure
        """
        if not self.is_production:
            key = API_KEY_TEST_ENV

        logger.debug("key=%s verify=%s" % (key, verify))
        sid = self.service.Zaloguj(key)
        session = Session()
        session.headers.update({"sid": sid})
        self.client = Client(
            wsdl=self.wsdl,
            transport=Transport(
                session=session,
                timeout=self.timeout,
                operation_timeout=self.operation_timeout,
            ),
        )
        self._create_service()
        if verify:
            if not self._check_session():
                logger.error("Authentication failed")
                raise ApiAuthenticationError(key)
            else:
                logger.debug("Authenticated successfully")
        self.key = key
        self.sid = sid
        return sid

    def get_last_code(self):
        """Gets Regon API status code of last performed operation

        Returns
        -------
        tuple
            a tuple (api_response : str, translated_message: str, dict)
            translated_message is dict when settings lang='all'
        """
        response = self.service.GetValue(pNazwaParametru="KomunikatKod")
        ret = response, t("GetValue", response)
        logger.debug(ret)
        return ret

    def get_data_status(self):
        """Gets Regon API data status

        Returns
        -------
        str
            date of last database update
        """
        response = self.service.GetValue(pNazwaParametru="StanDanych")
        logger.debug(response)
        return response

    def get_service_status(self):
        """Gets Regon API status code and status message

        Returns
        -------
        tuple
            a tuple (api_response : str, translated_message: str, dict)
            translated_message is dict when settings lang='all'
        """
        response = self.service.GetValue(pNazwaParametru="StatusUslugi")
        ret = response, t("ServiceStatus", response)
        logger.debug(ret)
        return ret

    def get_operations(self):
        """Gets all operations listed in WSDL

        Returns
        -------
        list
            of names of the operations
        """
        ret = list(self.service._operations.keys())
        logger.debug("WSDL operations: %s" % ret)
        return ret

    def __str__(self):
        """Prints attributes"""
        msg = """
            WSDL        : {service_url}
            Service URL : {wsdl}
            API key     : {key}
            sid         : {sid}
            ----------------------------------
            Data status : {data_status}
        """.format(
            wsdl=self.wsdl,
            service_url=self.service_url,
            key=self.key,
            sid=self.sid,
            data_status=self.get_data_status(),
        )
        return msg

    def _create_service(self):
        """Creates service with provided URL

        Note
        ----
        This method is called after self.client if modified in
        __init__ constructor and authenticate method.
        Service is available at self.service.
        """
        logger.debug("Creating service with url %s" % self.service_url)
        self.service = self.client.create_service(
            self.service_namespace, self.service_url
        )

    def _check_session(self):
        """Checks Regon API for confirmation of successfull authentication

        Returns
        -------
        bool
            True if authentication successfull, else False
        """
        response = self.service.GetValue(pNazwaParametru="StatusSesji")
        return True if response == "1" else False
