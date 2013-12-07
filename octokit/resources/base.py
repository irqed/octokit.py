# encoding: utf-8

"""
Base for GitHub API resources
"""

import requests


class Resource(object):
    """Base class for all GitHub API resources
    """
    def __init__(self, http, **kwargs):
        super(Resource, self).__init__()
        self._http = http
