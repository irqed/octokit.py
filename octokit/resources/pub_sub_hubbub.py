# encoding: utf-8

"""Methods for the PubSubHubbub API
http://developer.github.com/v3/repos/hooks/#pubsubhubbub
"""

from octokit.resources.base import Resource


class PubSubHubbub(Resource):
    """PubSubHubbub API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(PubSubHubbub, self).__init__(**kwargs)

    def subscribe(self):
        """Subscribe to a pubsub topic

        http://developer.github.com/v3/repos/hooks/#subscribing
        """
        raise NotImplementedError

    def unsubscribe(self):
        """Unsubscribe from a pubsub topic

        http://developer.github.com/v3/repos/hooks/#subscribing
        """
        raise NotImplementedError

    def subscribe_service_hook(self):
        """Subscribe to a repository through pubsub

        http://developer.github.com/v3/repos/hooks/#subscribing
        """
        raise NotImplementedError

    def unsubscribe_service_hook(self):
        """Unsubscribe repository through pubsub

        http://developer.github.com/v3/repos/hooks/#subscribing
        """
        raise NotImplementedError
