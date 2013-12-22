# encoding: utf-8

"""Github auth backends for requests.
"""

import json
import requests

from octokit.errors import OctokitError, OctokitNotFoundError


class HTTPBackend(object):
    """Wrapper for requests session
    """
    def __init__(self, settings):
        super(HTTPBackend, self).__init__()
        self._settings = settings
        self._s = requests.Session()
        self._s.proxies = self._settings.proxies
        self._s.trust_env = self._settings.trust_env

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

    def raise_if_any(self):
        if self.last_response.status_code == requests.codes.not_found:
            raise OctokitNotFoundError(self.last_response.status_code,
                                       self.last_response.json()['message'])
        elif not self.last_response.ok:
            raise OctokitError(self.last_response.status_code,
                               self.last_response.json()['message'])

    def _request(self, method, path, params=None, payload=None):
        url = self._settings.api_endpoint + path
        self.last_response = self._s.request(method, url, params=params,
                                             data=json.dumps(payload))
        self.raise_if_any()
        return self.last_response

    def boolean(self, method, path, params=None, payload=None):
        try:
            self._request(method, path, params, payload)
            if self.last_response.status_code == requests.codes.no_content:
                return True
        except OctokitNotFoundError:
            return False

    def get(self, path, params=None):
        return self._request('GET', path, params).json()

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def patch(self, path, **payload):
        data = {}
        for key, value in payload.items():
            data[key] = value
        return self._request('PATCH', path, payload=data).json()

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
