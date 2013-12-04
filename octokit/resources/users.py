# encoding: utf-8

"""
Methods for the Users API
"""

from .base import Resource


class User(Resource):
    """User API resource
    http://developer.github.com/v3/users/#get-the-authenticated-user
    """
    def __init__(self):
        super(User, self).__init__()


class Users(Resource):
    """Users API resource
    http://developer.github.com/v3/users/
    """
    def __init__(self):
        super(Users, self).__init__()
