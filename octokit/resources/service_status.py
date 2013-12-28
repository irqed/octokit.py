# encoding: utf-8

"""Methods for the GitHub Status API
https://status.github.com/api
"""

from octokit.resources.base import Resource


class ServiceStatus(Resource):
    """GitHub API service status 
    """
    url = 'https://status.github.com/api.json'

    def __init__(self, **kwargs):
        super(ServiceStatus, self).__init__(**kwargs)

    @property
    def status(self):
        return self._http._request('GET',
                    'https://status.github.com/api/status.json').json()

    @property
    def last_message(self):
        return self._http._request('GET',
                    'https://status.github.com/api/last-message.json').json()

    @property
    def messages(self):
        return self._http._request('GET',
                    'https://status.github.com/api/messages.json').json()
