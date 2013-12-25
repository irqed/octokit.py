# encoding: utf-8

"""Base for GitHub API resources
"""


class Resource(object):
    """Base class for all GitHub API resources
    """
    path = None

    def __init__(self, **kwargs):
        super(Resource, self).__init__()
        self._http = kwargs.get('http')
