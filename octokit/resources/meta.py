# encoding: utf-8

"""Methods for the Meta API
http://developer.github.com/v3/meta/
"""

from octokit.resources.base import Resource


class Meta(Resource):
    """Meta API resource
    """
    url = '/meta'

    def __init__(self, **kwargs):
        super(Meta, self).__init__(**kwargs)

    def meta(self):
        """Get meta information about GitHub.com, the service.
        http://developer.github.com/v3/meta/#meta
        """
        raise NotImplementedError
