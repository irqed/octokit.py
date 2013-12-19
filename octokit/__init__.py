# encoding: utf-8

#                           /~\   Hey you, wanna help?
#                          (O O) _/
#                          _\=/_
#          ___            /  _  \
#         / ()\          //|/.\|\\
#       _|_____|_       ||  \_/  ||
#      | | === | |      || |\ /| ||
#      |_|  O  |_|       # \_ _/ #
#       ||  O  ||          | | |
#       ||__*__||          | | |
#      |~ \___/ ~|         []|[]
#      /=\ /=\ /=\         | | |
#______[_]_[_]_[_]________/_]_[_\_____

"""
Octokit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Octokit is a python toolkit for the GitHub API.

:copyright: (c) 2013 by Alexander Shchepetilnikov.
:license: MIT, see LICENSE for more details.
"""

__version__ = '0.0.1'
__author__ = 'Alexander Shchepetilnikov'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Alexander Shchepetilnikov'


from octokit.client import Octokit
from octokit.http import OctokitError

__all__ = ['Octokit', 'OctokitError']
