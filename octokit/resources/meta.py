# encoding: utf-8

"""Methods for the Meta API
http://developer.github.com/v3/meta/
"""

from octokit.resources.base import Resource


class Meta(Resource):
    """Meta API resource
    """
    def __init__(self, **kwargs):
        super(Meta, self).__init__(**kwargs)

    def info(self):
        """Get meta information about GitHub.com, the service.

        http://developer.github.com/v3/meta/#meta
        """
        return self._http.get('meta')
