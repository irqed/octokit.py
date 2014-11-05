# encoding: utf-8

from requests import auth


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

    def __call__(self, r):
        return r
