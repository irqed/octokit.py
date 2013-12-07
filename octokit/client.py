# encoding: utf-8

"""
Toolkit for the GitHub API.
"""
import requests

from options import DEFAULTS, Options
from resources import (User, Users)


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


class OctokitError(Exception):
    """Custom exception to wrap API response errors
    """
    def __init__(self, message):
        super(OctokitError, self).__init__(message)


class HTTPBackend(object):
    """Wrapper for requests session
    """
    def __init__(self, options):
        super(HTTPBackend, self).__init__()
        self.session = requests.Session()

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class Octokit(object):
    """Brings all Github API resources together
    """
    def __init__(self, **kwargs):
        super(Octokit, self).__init__()
        self.merge_options(DEFAULTS, kwargs)
        self.http = HTTPBackend(self.options)

    def merge_options(self, defaults, options):
        self.options = Options(
            access_token=options.get('access_token') or defaults.access_token,

            client_id=options.get('client_id') or defaults.client_id,
            client_secret=options.get('client_secret') or defaults.client_secret,

            login=options.get('login') or defaults.login,
            password=options.get('password') or defaults.password,

            proxy=options.get('proxy') or defaults.proxy,

            api_endpoint=options.get('api_endpoint') or defaults.api_endpoint,
            web_endpoint=options.get('web_endpoint') or defaults.web_endpoint,

            user_agent=options.get('user_agent') or defaults.user_agent,
            media_type=options.get('media_type') or defaults.media_type,

            auto_paginate=options.get('auto_paginate') or defaults.auto_paginate,
            page_size=options.get('page_size') or defaults.page_size
        )

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
        return True if self.options.login and self.options.password else False

    @property
    def token_authenticated(self):
        return True if self.options.access_token else False

    @property
    def application_authenticated(self):
        return (True if self.options.client_id and
                        self.options.client_secret else False)

    @lazy_property
    def user(self):
        return User(self.http)

    @lazy_property
    def users(self):
        return Users(self.http)
