# encoding: utf-8

"""Custom error classes for GitHub responses.
"""


class OctokitError(Exception):
    """Base class to wrap up an API response error
    """
    def __init__(self, response):
        self.body = response.json()
        self.headers = response.headers
        self.code = response.status_code

        if 'message' in self.body:
            self.message = self.body.get('message')

        if 'errors' in self.body:
            self.errors = self.body.get('errors')

        super(OctokitError, self).__init__("%s %s" % (self.code, self.message))


class OctokitClientError(OctokitError):
    """Raised on errors in the 400-499 range
    """


class OctokitBadRequestError(OctokitError):
    """Raised when GitHub returns a 400 HTTP status code
    """


class OctokitUnauthorizedError(OctokitError):
    """Raised when GitHub returns a 401 HTTP status code
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


class OctokitConflictError(OctokitError):
    """Raised when GitHub returns a 409 HTTP status code
    """


class OctokitUnsupportedMediaTypeError(OctokitError):
    """Raised when GitHub returns a 414 HTTP status code
    """


class OctokitUnprocessableEntityError(OctokitError):
    """Raised when GitHub returns a 422 HTTP status code
    """


class OctokitServerError(OctokitError):
    """Raised on errors in the 500-599 range
    """


class OctokitInternalServerErrorError(OctokitError):
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


class OctokitMissingContentTypeError(OctokitError):
    """Raised when client fails to provide valid Content-Type
    """


def error_from_response(response, *args, **kwargs):
    """Raises appropriate error based on HTTP status code.
    """
    if response.status_code == 400:
        raise OctokitBadRequestError(response)
    elif response.status_code == 401:
        raise OctokitUnauthorizedError(response)
    elif response.status_code == 403:
        raise OctokitForbiddenError(response)
    elif response.status_code == 404:
        raise OctokitNotFoundError(response)
    elif response.status_code == 406:
        raise OctokitNotAcceptableError(response)
    elif response.status_code == 409:
        raise OctokitConflictError(response)
    elif response.status_code == 415:
        raise OctokitUnsupportedMediaTypeError(response)
    elif response.status_code == 422:
        raise OctokitUnprocessableEntityError(response)
    elif 400 <= response.status_code <= 499:
        raise OctokitClientError(response)
    elif response.status_code == 500:
        raise OctokitInternalServerErrorError(response)
    elif response.status_code == 501:
        raise OctokitNotImplementedError(response)
    elif response.status_code == 502:
        raise OctokitBadGatewayError(response)
    elif response.status_code == 503:
        raise OctokitServiceUnavailableError(response)
    elif 500 <= response.status_code <= 599:
        raise OctokitServerError(response)

    return response
