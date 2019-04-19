import logging

from zeep.transports import Transport
from zeep import Client
from requests import Session

from RegonAPI.exceptions import ApiAuthenticationError
from RegonAPI.api_codes import t
from RegonAPI.operations import RegonAPIOperations

from RegonAPI.settings import logging_level
from RegonAPI.settings import logging_file_handler_level
from RegonAPI.settings import logging_stream_handler_level

# logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging_level)

# fh = logging.FileHandler('debug.log')
# fh.setLevel(logging_file_handler_level)

sh = logging.StreamHandler()
sh.setLevel(logging_stream_handler_level)

formatter = logging.Formatter(
    '[%(levelname)s][%(asctime)s] %(name)s %(funcName)s - %(message)s')
# fh.setFormatter(formatter)
sh.setFormatter(formatter)

# logger.addHandler(fh)
logger.addHandler(sh)
# logger configuration End


class RegonAPI(RegonAPIOperations):
    """Regon API client

    Parameters
    ----------
    wsdl : str
        Regon API WSDL (Web Services Description Language) URL
    service_url : str
        Service URL provided by RegonAPI Administrators
    service_namespace : str
        Service namespace default: {http://tempuri.org/}e3

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

    def __init__(self, wsdl, service_url,
                 service_namespace='{http://tempuri.org/}e3'):
        logger.debug('wsdl=%s service_url=%s' % (wsdl, service_url))
        self.service_namespace = service_namespace
        self.client = Client(wsdl=wsdl)
        self.wsdl = wsdl
        self.service_url = service_url
        self.service = None
        self.key = None
        self.sid = None
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
        logger.debug('key=%s verify=%s' % (key, verify))
        sid = self.service.Zaloguj(key)
        session = Session()
        session.headers.update({'sid': sid})
        self.client = Client(
            wsdl=self.wsdl,
            transport=Transport(session=session)
        )
        self._create_service()
        if verify:
            if not self._check_session():
                logger.warning('Authentication failed')
                raise ApiAuthenticationError(key)
            else:
                logger.debug('Authenticated successfully')
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
        response = self.service.GetValue(pNazwaParametru='KomunikatKod')
        ret = response, t('GetValue', response)
        logger.debug(ret)
        return ret

    def get_data_status(self):
        """Gets Regon API data status

        Returns
        -------
        str
            date of last database update
        """
        response = self.service.GetValue(pNazwaParametru='StanDanych')
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
        response = self.service.GetValue(pNazwaParametru='StatusUslugi')
        ret = response, t('ServiceStatus', response)
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
        logger.debug('Creating service with url %s' % self.service_url)
        self.service = self.client.create_service(
            self.service_namespace, self.service_url)

    def _check_session(self):
        """Checks Regon API for confirmation of successfull authentication

        Returns
        -------
        bool
            True if authentication successfull, else False
        """
        response = self.service.GetValue(pNazwaParametru='StatusSesji')
        return True if response == '1' else False
