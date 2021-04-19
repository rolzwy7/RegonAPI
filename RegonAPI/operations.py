"""
    Extends RegonAPI with operations
"""

from .parsers import parse_xml_response
from .exceptions import ApiUnknownReportNameError, ApiInvalidDateFormat
from . import validators
from .settings import OPERATIONS


class RegonAPIOperations(object):
    def searchData(
        self,
        krs=None,
        regon=None,
        nip=None,
        regons9=None,
        regons14=None,
        krss=None,
        nips=None,
    ):
        """Search data

        Parameters
        ----------
        krs : str
            KRS number
        regon : str
            REGON9 or REGON14
        nip : str
            NIP number
        regons9 : list
            List of REGON9 numbers
        regons14 : list
            List of REGON14 numbers
        krss : list
            List of KRS numbers
        nips : list
            List of NIP numbers

        Returns
        -------
        None
            If not found any results for provided parameters
        list
            List of results

        Raises
        ------
        Exception
            If no parameters provided
        TypeError
            If at least one parameter is provided with incorrect type
        """
        # Validate parameters
        str_params = [krs, regon, nip]
        list_params = [regons9, regons14, krss, nips]
        if not any(str_params) and not any(list_params):
            raise Exception("provide at least one parameter")

        if krs is not None and not isinstance(krs, str):
            raise TypeError("krs - invalid (str required)")
        if regon is not None and not isinstance(regon, str):
            raise TypeError("regon - invalid (str required)")
        if nip is not None and not isinstance(nip, str):
            raise TypeError("nip - invalid (str required)")

        if regons9 is not None and not isinstance(regons9, list):
            raise TypeError("regons9 - invalid (list required)")
        if regons14 is not None and not isinstance(regons14, list):
            raise TypeError("regons14 - invalid (list required)")
        if krss is not None and not isinstance(krss, list):
            raise TypeError("krss - invalid (list required)")
        if nips is not None and not isinstance(nips, list):
            raise TypeError("nips - invalid (list required)")

        if regons9 is not None:
            for _ in regons9:
                validators.is_valid_regon9(_)

        if regons14 is not None and not isinstance(regons14, list):
            for _ in regons9:
                validators.is_valid_regon14(_)

        # NIP validation

        # KRS validation

        # Validate parameters - End

        # join lists
        regons9 = ",".join(regons9) if regons9 else None
        regons14 = ",".join(regons14) if regons14 else None
        krss = ",".join(krss) if krss else None
        nips = ",".join(nips) if nips else None
        # join lists - End

        search_param = "pParametryWyszukiwania"
        request_data = {search_param: {}}
        map_ = {
            "krs": "Krs",
            "regon": "Regon",
            "nip": "Nip",
            "regons9": "Regony9zn",
            "regons14": "Regony14zn",
            "krss": "Krsy",
            "nips": "Nipy",
        }
        for k, v in locals().items():
            if k in map_.keys():
                if v is not None:
                    request_data[search_param][map_[k]] = v

        wsdl_method = getattr(
            self.service, OPERATIONS["alias_search_data"][self.bir_version]
        )
        response = wsdl_method(**request_data)
        return parse_xml_response(response) if response else None

    def dataDownloadFullReport(self, regon, report_name, strict=True):
        """Search data (DaneSzukaj wrapper)

        Parameters
        ----------
        regon : str
            REGON9 or REGON14
        report_name : str
            report name
        strict : bool
            If True checks if report_name is valid (default: True)

        Returns
        -------
        None
            If not found any results for provided parameters
        list
            List of results

        Raises
        ------
        ApiUnknownReportNameError
            If strict=True and provided report name is not included in
            predefined list of valid report names
        """
        if strict is True and report_name not in self.reports:
            raise ApiUnknownReportNameError(report_name)
        request_data = {"pRegon": regon, "pNazwaRaportu": report_name}
        wsdl_method = getattr(
            self.service,
            OPERATIONS["alias_data_download_full_report"][self.bir_version],
        )
        response = wsdl_method(**request_data)
        return parse_xml_response(response) if response else None

    def dataDownloadFullGroupReport(self, report_date, report_name, strict=True):
        """
        DanePobierzRaportZbiorczy wrapper

        Parameters
        ----------
        report_date : str
            date string in format yyyy-mm-dd
        report_name : str
            report name
        strict : bool
            If True checks if report_name is valid (default: True)

        Returns
        -------
        None
            If not found any results for provided parameters
        list
            List of results

        Raises
        ------
        ApiUnknownReportNameError
            If strict=True and provided report name is not included in
            predefined list of valid report names or report date is in
            invalid format
        """
        if strict is True:
            if report_name not in self.reports:
                raise ApiUnknownReportNameError(report_name)
            if validators.is_valid_date(report_date) is False:
                raise ApiInvalidDateFormat(report_date)

        request_data = {"pDataRaportu": report_date, "pNazwaRaportu": report_name}
        wsdl_method = getattr(
            self.service,
            OPERATIONS["alias_data_download_full_group_report"][self.bir_version],
        )
        response = wsdl_method(**request_data)
        return parse_xml_response(response) if response else None
