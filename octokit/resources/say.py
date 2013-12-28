# encoding: utf-8

"""Methods for the unpublished Octocat API

A nifty ASCII Octocat with GitHub wisdom:)
"""

from octokit.resources.base import Resource


class Say(Resource):
    """Say API resource
    """
    def __init__(self, **kwargs):
        super(Say, self).__init__(**kwargs)

    def octocat(self, text=None):
        """Return a nifty ASCII Octocat with GitHub wisdom or your own
        """
        say = text if text else None
        return self._http._request('GET',
                self._http._settings.api_endpoint + 'octocat', payload=say).text
