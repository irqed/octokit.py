# encoding: utf-8

"""Methods for the Authorizations API
http://developer.github.com/v3/oauth/#oauth-authorizations-api
"""

from octokit.resources.base import Resource


class Authorizations(Resource):
    """Authorizations API resource
    """
    url = '/authorizations'

    def __init__(self, **kwargs):
        super(Authorizations, self).__init__(**kwargs)
