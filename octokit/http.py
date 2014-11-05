# encoding: utf-8

"""Github auth backends for requests.
"""

import json
import requests

from .errors import error_from_response, OctokitNotFoundError


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
        self._s.headers['Content-Type'] = 'application/json'

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

    def _request(self, method, url, params=None, payload=None, **kwargs):
        hooks = dict(response=error_from_response)
        allow_redirects = kwargs.get('allow_redirects')
        self.last_response = self._s.request(method, url,
                                             params=params, hooks=hooks,
                                             data=json.dumps(payload),
                                             allow_redirects=allow_redirects)

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
        return self._request('POST', self.full_url(path),
                             payload=payload).json()

    def put(self, path, payload):
        return self._request('PUT', self.full_url(path),
                             payload=payload).json()

    def patch(self, path, payload):
        return self._request('PATCH', self.full_url(path),
                             payload=payload).json()

    def delete(self, path, payload=None):
        return self._request('DELETE', self.full_url(path),
                             payload=payload).json()

    def head(self, path, params=None, allow_redirects=True):
        return self._request('HEAD', self.full_url(path),
                             params=params, allow_redirects=allow_redirects)
