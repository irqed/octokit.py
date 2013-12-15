# encoding: utf-8

"""Methods for the Users API
"""

from octokit.resources.base import Resource


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

    def get(self, **kwargs):
        login = kwargs.get('login')
        if login:
            return self._http.get(self.url + "/%s" % login)
        else:
            return self._http.get(self.url)
