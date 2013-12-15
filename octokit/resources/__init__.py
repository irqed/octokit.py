# encoding: utf-8

"""GitHub API resources.
"""

from octokit.resources.users import User, Users
from octokit.resources.authorizations import Authorizations

__all__ = ['User', 'Users', 'Authorizations']
