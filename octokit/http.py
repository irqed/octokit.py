# encoding: utf-8

"""Github auth backends for requests.
"""

import requests


class OctokitError(Exception):
    """Custom exception to wrap API response errors
    """
    def __init__(self, message):
        super(OctokitError, self).__init__(message)


class HTTPBackend(object):
    """Wrapper for requests session
    """
    def __init__(self, settings):
        super(HTTPBackend, self).__init__()
        self._settings = settings
        self._session = requests.Session()

        self.last_request = None
        self.last_response = None

        self.setup_headers()
        self.setup_auth()

    def setup_headers(self):
        self._session.headers['Accept'] = self._settings.media_type
        self._session.headers['User-Agent'] = self._settings.user_agent

    def setup_auth(self):
        if self._settings.login and self._settings.password:
            self._session.auth = HTTPBasicAuth(self._settings.login,
                                      self._settings.password)
        elif self._settings.access_token:
            self._session.auth = HTTPTokenAuth(self._settings.access_token)
        elif self._settings.client_id and self._settings.client_secret:
            self._session.auth = HTTPApplicationAuth(self._settings.client_id,
                                            self._settings.client_secret)

    @property
    def auth(self):
        return self._session.auth if self._session.auth else None

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class HTTPBasicAuth(requests.auth.AuthBase):
    """Class to use with GitHub basic auth
    """
    def __init__(self, login, password):
        super(HTTPBasicAuth, self).__init__()


class HTTPTokenAuth(requests.auth.AuthBase):
    """Class to use with GitHub's access_token
    """
    def __init__(self, access_token):
        super(HTTPTokenAuth, self).__init__()


class HTTPApplicationAuth(requests.auth.AuthBase):
    """Class to use with GitHub's application auth
    """
    def __init__(self, client_id, client_secret):
        super(HTTPApplicationAuth, self).__init__()
