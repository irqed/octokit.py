# encoding: utf-8

"""Methods for the GitHub Status API
https://status.github.com/api
"""

from octokit.resources.base import Resource


class ServiceStatus(Resource):
    """GitHub API service status 
    http://developer.github.com/v3/users/#get-the-authenticated-user
    """
    url = '/api/status.json'

    def __init__(self, **kwargs):
        super(ServiceStatus, self).__init__(**kwargs)

    @property
    def status(self):
        return self._http.get('/api/status.json')

    @property
    def last_message(self):
        return self._http.get('/api/last-message.json')

    @property
    def messages(self):
        return self._http.get('/api/messages.json')
