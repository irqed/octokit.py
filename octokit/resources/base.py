# encoding: utf-8

"""Base for GitHub API resources
"""

import json


class Resource(object):
    """Base class for all GitHub API resources
    """
    def __init__(self, **kwargs):
        super(Resource, self).__init__()
        self._http = kwargs.get('http')

    def get(self):
        return self._http.get(self.url)
