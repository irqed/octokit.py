# encoding: utf-8

"""Methods for the Authorizations API
"""

from octokit.resources.base import Resource


class Authorizations(Resource):
    """Authorizations API resource
    http://developer.github.com/v3/oauth/#oauth-authorizations-api
    """
    url = '/authorizations'

    def __init__(self, **kwargs):
        super(Authorizations, self).__init__(**kwargs)
