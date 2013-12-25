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

    def _get(self, path):
        return self._http.get(path)

    def _list(self):
        raise NotImplementedError

    def _update(self, path, payload):
        return self._http.patch(path, payload)

    def _create(self):
        raise NotImplementedError

    def _remove(self):
        raise NotImplementedError
