# encoding: utf-8

"""Toolkit for the GitHub API.
"""

import slumber
import requests

from .auth import BasicAuth, TokenAuth, ApplicationAuth
from .settings import Settings


class Octokit(slumber.API):
    """Github resources hub. Brings everything together.
    """
    def __init__(self, **kwargs):
        self.settings = Settings(**kwargs)

        self._session = requests.Session()
        self._session.proxies = self.settings.proxies
        self._session.trust_env = self.settings.trust_env

        self.__setup_headers()
        self.__setup_auth()

        super(Octokit, self).__init__(
            append_slash=False,
            session=self._session,
            base_url=self.settings.api_endpoint,
        )

    def __setup_headers(self):
        self._session.headers['Accept'] = self.settings.media_type
        self._session.headers['User-Agent'] = self.settings.user_agent
        self._session.headers['Content-Type'] = 'application/json'

    def __setup_auth(self):
        if self.settings.access_token:
            self._session.auth = TokenAuth(self.settings.access_token)

        elif self.settings.login and self.settings.password:
            self._session.auth = BasicAuth(
                self.settings.login,
                self.settings.password
            )

        elif self.settings.client_id and self.settings.client_secret:
            self._session.auth = ApplicationAuth(
                self.settings.client_id,
                self.settings.client_secret
            )

    @property
    def auth(self):
        return self._session.auth if self._session.auth else None

    @property
    def basic_authenticated(self):
        return (True if isinstance(self.auth, BasicAuth)
                else False)

    @property
    def token_authenticated(self):
        return (True if isinstance(self.auth, TokenAuth)
                else False)

    @property
    def application_authenticated(self):
        return (True if isinstance(self.auth, ApplicationAuth)
                else False)

    @property
    def user_authenticated(self):
        return self.basic_authenticated or self.token_authenticated

    @property
    def authenticated(self):
        return (self.user_authenticated or
                self.application_authenticated)
