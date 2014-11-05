# encoding: utf-8

"""Settings class and default values for an API client.
"""

from os import environ
from .version import __version__


# Default API endpoint
API_ENDPOINT = "https://api.github.com/"

# Default WEB endpoint
WEB_ENDPOINT = "https://github.com"

# Default User Agent header string
USER_AGENT = "octokit.py/%s" % __version__

# Default media type
MEDIA_TYPE = "application/vnd.github.beta+json"

# Default page size
PAGE_SIZE = 50

# Do not auto paginate by default
AUTO_PAGINATE = False

# Can we trust env or not
TRUST_ENV = True

# Verify SSL certificate
VERIFY_SSL = True


class Settings(object):
    """Octokit settings class.
    """
    def __init__(self, **kwargs):
        super(Settings, self).__init__()
        self.verify = kwargs.get('verify', VERIFY_SSL)
        self.trust_env = kwargs.get('trust_env', TRUST_ENV)

        self.login = kwargs.get('login')
        self.password = kwargs.get('password')

        self.access_token = kwargs.get('access_token')

        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')

        self.proxies = kwargs.get('proxies')

        self.api_endpoint = kwargs.get('api_endpoint', API_ENDPOINT)
        self.web_endpoint = kwargs.get('web_endpoint', WEB_ENDPOINT)

        self.user_agent = kwargs.get('user_agent', USER_AGENT)
        self.media_type = kwargs.get('media_type', MEDIA_TYPE)

        self.auto_paginate = kwargs.get('auto_paginate', AUTO_PAGINATE)
        self.page_size = int(kwargs.get('page_size', PAGE_SIZE))

        if not self.is_credentials_passed and self.trust_env:
            self.set_from_env()

    @property
    def is_credentials_passed(self):
        if ((self.login and self.password) or self.access_token or
                (self.client_id and self.client_secret)):
            return True
        return False

    def set_from_env(self):
        self.login = environ.get('OCTOKIT_LOGIN')
        self.password = environ.get('OCTOKIT_PASSWORD')

        self.access_token = environ.get('OCTOKIT_ACCESS_TOKEN')

        self.client_id = environ.get('OCTOKIT_CLIENT_ID')
        self.client_secret = environ.get('OCTOKIT_SECRET')
