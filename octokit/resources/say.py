# encoding: utf-8

"""Methods for the unpublished Octocat API

A nifty ASCII Octocat with GitHub wisdom:)
"""

from octokit.resources.base import Resource


class Say(Resource):
    """Say API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Say, self).__init__(**kwargs)

    def say(self):
        """Return a nifty ASCII Octocat with GitHub wisdom or your own
        """
