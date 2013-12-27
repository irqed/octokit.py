# encoding: utf-8

"""Toolkit for the GitHub API.
"""

from octokit import http
from octokit.settings import Settings
from octokit.resources import (Authorizations, Emojis, Gists, Gitignore, Meta,
                               ServiceStatus, User, Users)


def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated
    """
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property


class Octokit(object):
    """Github API resources hub. Brings everything together.
    """
    def __init__(self, **kwargs):
        super(Octokit, self).__init__()
        self.settings = Settings(**kwargs)
        self._http = http.HTTPBackend(self.settings)

    @property
    def authenticated(self):
        return (self.basic_authenticated or
                self.token_authenticated or
                self.application_authenticated)

    @property
    def user_authenticated(self):
        return self.basic_authenticated or self.token_authenticated

    @property
    def basic_authenticated(self):
        return (True if isinstance(self._http.auth, http.HTTPBasicAuth)
                else False)

    @property
    def token_authenticated(self):
        return (True if isinstance(self._http.auth, http.HTTPTokenAuth)
                else False)

    @property
    def application_authenticated(self):
        return (True if isinstance(self._http.auth, http.HTTPApplicationAuth)
                else False)

    @lazy_property
    def authorizations(self):
        return Authorizations(http=self._http)

    @lazy_property
    def user(self):
        return User(http=self._http)

    @lazy_property
    def users(self):
        return Users(http=self._http)

    @lazy_property
    def emojis(self):
        return Emojis(http=self._http)

    @lazy_property
    def gists(self):
        return Gists(http=self._http)

    @lazy_property
    def gitignore(self):
        return Gitignore(http=self._http)

    @lazy_property
    def meta(self):
        return Meta(http=self._http)

    @lazy_property
    def service_status(self):
        return ServiceStatus(http=self._http)
