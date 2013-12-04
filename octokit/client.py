# encoding: utf-8

"""
Toolkit for the GitHub API.
"""

from octokit.options import DEFAULTS


class Octokit(object):
    """Brings all Github API resources together
    """
    def __init__(self, **kwargs):
        # TODO: merge default settings with kwargs

    @property
    def authenticated(self):
        return (self.basic_authenticated or
                self.token_authenticated or
                self.application_authenticated)

    @property
    def basic_authenticated(self):
        return (True if hasattr(self, 'login') and
                    hasattr(self, 'password') else False)

    @property
    def token_authenticated(self):
        return True if hasattr(self, 'access_token') else False

    @property
    def application_authenticated(self):
        return (True if hasattr(self, 'client_id') and
                    hasattr(self, 'client_secret') else False)
