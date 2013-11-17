# encoding: utf-8

"""
Client for the GitHub API.
"""

from octokit.client.default import DEFAULTS


class Client(object):
    """Client for the GitHub API
    """

    def __init__(self):
        self.__defaults = DEFAULTS

    def __is_same_options(self):
        """ Determine if the options for a new instance are the same or not
        """
        raise NotImplementedError
