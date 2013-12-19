# encoding: utf-8

"""Github auth backends for requests.
"""

import json
import requests


class OctokitError(Exception):
    """Custom exception to wrap API response errors
    """
    def __init__(self, code, message):
        super(OctokitError, self).__init__(message)
        self.code = code
        self.message = message


class HTTPBackend(object):
    """Wrapper for requests session
    """
    def __init__(self, settings):
        super(HTTPBackend, self).__init__()
        self._settings = settings
        self._s = requests.Session()
        self._s.proxies = self._settings.proxies
        self._s.trust_env = self._settings.trust_env

        self.last_request = None
        self.last_response = None

        self.setup_headers()
        self.setup_auth()

    def setup_headers(self):
        self._s.headers['Accept'] = self._settings.media_type
        self._s.headers['User-Agent'] = self._settings.user_agent

    def setup_auth(self):
        if self._settings.login and self._settings.password:
            self._s.auth = HTTPBasicAuth(self._settings.login,
                                         self._settings.password)
        elif self._settings.access_token:
            self._s.auth = HTTPTokenAuth(self._settings.access_token)
        elif self._settings.client_id and self._settings.client_secret:
            self._s.auth = HTTPApplicationAuth(self._settings.client_id,
                                               self._settings.client_secret)

    @property
    def auth(self):
        return self._s.auth if self._s.auth else None

    def get(self, url, params=None):
        url = url if 'https' in url else self._settings.api_endpoint + url
        r = self._s.get(url, auth=self.auth, params=params)
        if not r.ok:
            raise OctokitError(r.status_code, r.json()['message'])
        return r.json()

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def patch(self, url, **payload):
        data = {}
        for key, value in payload.items():
            data[key] = value
        r = self._s.patch(self._settings.api_endpoint + url, auth=self.auth,
                        data=json.dumps(data))
        if not r.ok:
            raise OctokitError(r.status_code, r.json()['message'])
        return r.json()

    def delete(self):
        raise NotImplementedError


class HTTPBasicAuth(requests.auth.HTTPBasicAuth):
    """Class to use with GitHub basic auth
    """
    def __init__(self, login, password):
        super(HTTPBasicAuth, self).__init__(login, password)


class HTTPTokenAuth(requests.auth.AuthBase):
    """Class to use with GitHub's access_token
    """
    def __init__(self, access_token):
        super(HTTPTokenAuth, self).__init__()
        self.access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'token %s' % self.access_token
        return r


class HTTPApplicationAuth(requests.auth.AuthBase):
    """Class to use with GitHub's application auth
    """
    def __init__(self, client_id, client_secret):
        super(HTTPApplicationAuth, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret

    def __call__(self, r):
        return r
