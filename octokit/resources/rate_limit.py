# encoding: utf-8

"""Methods for API rate limiting info
http://developer.github.com/v3/#rate-limiting
"""

from octokit.resources.base import Resource


class RateLimit(Resource):
    """RateLimit API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(RateLimit, self).__init__(**kwargs)

    def rate_limit(self):
        """Refresh rate limit info by making a new request

        http://developer.github.com/v3/rate_limit/#rate-limit
        """

        raise NotImplementedError
