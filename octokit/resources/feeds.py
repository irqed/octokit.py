# encoding: utf-8

"""Methods for the Feeds API

http://developer.github.com/v3/activity/feeds/
"""

from octokit.resources.base import Resource


class Feeds(Resource):
    """Feeds API resource
    """
    def __init__(self, **kwargs):
        super(Feeds, self).__init__(**kwargs)

    def all(self):
        """List Feeds

        http://developer.github.com/v3/activity/feeds/#list-feeds
        """
        return self._http.get('feeds')

    def feed(self):
        """Get a Feed by name
        """
        raise NotImplementedError
