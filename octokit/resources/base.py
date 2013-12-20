# encoding: utf-8

"""Base for GitHub API resources
"""


class Resource(object):
    """Base class for all GitHub API resources
    """
    url = None

    def __init__(self, **kwargs):
        super(Resource, self).__init__()
        self._http = kwargs.get('http')

    def get(self):
        return self._http.get(self.url)

    def list(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def create(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError
