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

    def get(self, **kwargs):
        auth_id = kwargs.get('id')
        if auth_id:
            return self._http.get(self.url + "/%s" % auth_id)
        else:
            return self._http.get(self.url)

    def create_authorization(self):
        """You can create your own tokens, and only through
        http://developer.github.com/v3/oauth/#create-a-new-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def update_authorization(self):
        """Update an authorization for the authenticated user.
        http://developer.github.com/v3/oauth/#update-a-new-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def delete_authorization(self):
        """Delete an authorization for the authenticated user
        http://developer.github.com/v3/oauth/#delete-an-authorization
        """
        raise NotImplementedError

    def scopes(self):
        """Check scopes for a token
        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def authorize_url(self):
        """Get the URL to authorize a user for an application via the web flow
        http://developer.github.com/v3/oauth/#web-application-flow
        """
        raise NotImplementedError
