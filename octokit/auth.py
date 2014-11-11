# encoding: utf-8

"""Classes to support GitHub auth methods.
"""

import urllib

from requests import auth

try:
    from urllib.parse import urlparse, parse_qsl, urlunparse
except ImportError:
    from urlparse import urlparse, parse_qsl, urlunparse


class BasicAuth(auth.HTTPBasicAuth):
    """Class to use with GitHub basic auth.
    """
    def __init__(self, login, password):
        super(BasicAuth, self).__init__(login, password)


class TokenAuth(auth.AuthBase):
    """Class to use with GitHub access_token.
    """
    def __init__(self, access_token):
        super(TokenAuth, self).__init__()
        self.access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'token %s' % self.access_token
        return r


class ApplicationAuth(auth.AuthBase):
    """Class to use with GitHub application auth.
    """
    def __init__(self, client_id, client_secret):
        super(ApplicationAuth, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret

    def __build_url(self, url):
        """Adds client_id and client_secret to query string
        """
        auth_params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(auth_params)

        url_parts[4] = urllib.urlencode(query)

        return urlunparse(url_parts)

    def __call__(self, r):
        r.url = self.__build_url(r.url)
        return r
