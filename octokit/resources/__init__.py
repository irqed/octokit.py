# encoding: utf-8

"""GitHub API resources.
"""

from octokit.resources.users import User, Users
from octokit.resources.authorizations import Authorizations
from octokit.resources.emojis import Emojis
from octokit.resources.gitignore import Gitignore
from octokit.resources.meta import Meta
from octokit.resources.service_status import ServiceStatus


__all__ = ['User', 'Users', 'Authorizations', 'Emojis', 'Gitignore', 'Meta',
           'ServiceStatus']
