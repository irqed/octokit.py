# encoding: utf-8

"""Custom error classes for the GitHub API.
"""


def error_from_responce(r, *args, **kwargs):
    pass


class OctokitError(Exception):
    """Custom exception to wrap up an API response error
    """
    def __init__(self, code, message):
        super(OctokitError, self).__init__("<%s> %s" % (code, message))
        self.code = code
        self.message = message


class OctokitClientError(OctokitError):
    """Raised on errors in the 400-499 range
    """


class OctokitBadRequestError(OctokitError):
    """Raised when GitHub returns a 400 HTTP status code
    """


class OctokitForbiddenError(OctokitError):
    """Raised when GitHub returns a 403 HTTP status code
    """


class OctokitTooManyRequestsError(OctokitError):
    """Raised when GitHub returns a 403 HTTP status code
    and body matches 'rate limit exceeded'
    """


class OctokitTooManyLoginAttemptsError(OctokitError):
    """Raised when GitHub returns a 403 HTTP status code
    and body matches 'login attempts exceeded'
    """


class OctokitNotFoundError(OctokitError):
    """Raised when GitHub returns a 404 HTTP status code
    """


class OctokitNotAcceptableError(OctokitError):
    """Raised when GitHub returns a 406 HTTP status code
    """


class OctokitUnsupportedMediaTypeError(OctokitError):
    """Raised when GitHub returns a 414 HTTP status code
    """


class OctokitUnprocessableEntityError(OctokitError):
    """Raised when GitHub returns a 422 HTTP status code
    """


class OctokitServerError(OctokitError):
    """Raised when GitHub returns a 500 HTTP status code
    """


class OctokitServerError(OctokitError):
    """Raised when GitHub returns a 500 HTTP status code
    """


class OctokitNotImplementedError(OctokitError):
    """Raised when GitHub returns a 500 HTTP status code
    """


class OctokitBadGatewayError(OctokitError):
    """Raised when GitHub returns a 502 HTTP status code
    """


class OctokitServiceUnavailableError(OctokitError):
    """Raised when GitHub returns a 503 HTTP status code
    """


class OctokitServiceUnavailableError(OctokitError):
    """Raised when client fails to provide valid Content-Type
    """
