# encoding: utf-8

"""GitHub API resources.
"""

from octokit.resources.users import User, Users
from octokit.resources.authorizations import Authorizations
from octokit.resources.emojis import Emojis
from octokit.resources.gitignore import Gitignore


__all__ = ['User', 'Users', 'Authorizations', 'Emojis', 'Gitignore']
