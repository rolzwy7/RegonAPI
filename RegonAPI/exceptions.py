

# -------------------------------------------------
# Api
# -------------------------------------------------
class ApiError(BaseException):
    def __str__(self):
        return repr(self.data)


class ApiAuthenticationError(ApiError):

    def __init__(self, data):
        self.data = 'Authentication failed with key: "{data}"'.format(
            data=data)


class ApiCodeTranslationError(ApiError):

    def __init__(self, data):
        self.data = 'Can\'t translate: {data}'.format(
            data=data)


class ApiUnknownReportNameError(ApiError):

    def __init__(self, data):
        self.data = 'Invailid report name: {data}'.format(
            data=data)


# -------------------------------------------------
# Converters
# -------------------------------------------------
class ConvertionTypeError(BaseException):

    def __init__(self, data, what=''):
        self.data = 'Can\'t convert {what}: {data}'.format(
            data=data, what=what)

    def __str__(self):
        return repr(self.data)


class ConvertionLengthError(BaseException):

    def __init__(self, data, what=''):
        self.data = 'Invalid {what} length: {data}'.format(
            data=data, what=what)

    def __str__(self):
        return repr(self.data)


class RegonConvertionError(ConvertionTypeError):

    def __init__(self, data):
        super(RegonConvertionError, self).__init__(
            data=data, what='regon'
        )
