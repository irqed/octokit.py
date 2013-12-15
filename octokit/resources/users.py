# encoding: utf-8

"""Methods for the Users API
"""

from base import Resource

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


class User(Resource):
    """User API resource
    http://developer.github.com/v3/users/#get-the-authenticated-user
    """
    url = '/user'

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Users(Resource):
    """Users API resource
    http://developer.github.com/v3/users/
    """
    url = '/users'

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def get(self, login=None):
        if login:
            return self._http.get(self.url + "/%s" % login)
        else:
            return self._http.get(self.url)
