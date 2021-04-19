from RegonAPI.settings import DATE_FORMAT


class ApiError(BaseException):
    def __str__(self):
        return repr(self.data)


class ApiAuthenticationError(ApiError):
    def __init__(self, data):
        self.data = 'Authentication failed with key: "{data}"'.format(data=data)


class ApiCodeTranslationError(ApiError):
    def __init__(self, data):
        self.data = "Can't translate: {data}".format(data=data)


class ApiUnknownReportNameError(ApiError):
    def __init__(self, data):
        self.data = "Invailid report name: {data}".format(data=data)


class ApiInvalidBIRVersionProvided(ApiError):
    def __init__(self, data, choices):
        self.data = "Invailid BIR version: {data} not in {choices}".format(
            data=data, choices=choices
        )


class ApiInvalidDateFormat(ApiError):
    def __init__(self, data):
        self.data = "Invalid date format given: '{data}'. Should be in '{correct_format}' format".format(
            data=data, correct_format=DATE_FORMAT
        )
