# encoding: utf-8

"""Github auth backends for requests.
"""

import json
import requests

from octokit.errors import error_from_response, OctokitNotFoundError


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

    def full_url(self, path):
        return self._settings.api_endpoint + path

    def _request(self, method, url, params=None, payload=None):
        hooks = dict(response=error_from_response)
        self.last_response = self._s.request(method, url,
                                             params=params, hooks=hooks,
                                             data=json.dumps(payload))

        return self.last_response

    def boolean_from_response(self, method, path, params=None, payload=None):
        try:
            self._request(method, self.full_url(path), params, payload)
            if self.last_response.status_code == requests.codes.no_content:
                return True
        except OctokitNotFoundError:
            return False

    def get(self, path, params=None):
        return self._request('GET', self.full_url(path), params=params).json()

    def post(self, path, payload=None):
        return self._request('POST', self.full_url(path), payload=payload).json()

    def put(self):
        return self._request('PUT', self.full_url(path), payload=payload).json()

    def patch(self, path, payload):
        return self._request('PATCH', self.full_url(path), payload=payload).json()

    def delete(self, payload=None):
        return self._request('DELETE', self.full_url(path), payload=payload).json()


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
