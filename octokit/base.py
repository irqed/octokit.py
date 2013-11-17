# encoding: utf-8

"""
Toolkit for the GitHub API.
"""

from octokit.client import Client


class Octokit(object):
    """Toolkit for the Github API
    """
    def __init__(self):
        self._client = Client()
