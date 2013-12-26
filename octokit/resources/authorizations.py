# encoding: utf-8

"""Methods for the Authorizations API

API for users to manage their own tokens.
You can only access your own tokens, and only through Basic Authentication.

http://developer.github.com/v3/oauth/#oauth-authorizations-api
"""

from octokit.resources.base import Resource


class Authorizations(Resource):
    """Authorizations API resource
    """
    def __init__(self, **kwargs):
        super(Authorizations, self).__init__(**kwargs)

    def all(self):
        """List the authenticated user's authorizations.

        You can only access your own tokens, and only through 
        Basic Authentication.

        http://developer.github.com/v3/oauth/#list-your-authorizations
        """
        return self._http.get('authorizations')

    def authorization(self, auth_id):
        """Get a single authorization for the authenticated user.

        You can only access your own tokens, and only through 
        Basic Authentication.


        http://developer.github.com/v3/oauth/#get-a-single-authorization
        """
        return self._http.get('authorizations/%s' % auth_id)

    def create(self, auth_data):
        """You can create your own tokens, and only through

        You can only access your own tokens, and only through 
        Basic Authentication.

        http://developer.github.com/v3/oauth/#create-a-new-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def update(self, auth_id, auth_data):
        """Update an authorization for the authenticated user.

        You can only access your own tokens, and only through 
        Basic Authentication.


        http://developer.github.com/v3/oauth/#update-a-new-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def delete(self, auth_id):
        """Delete an authorization for the authenticated user

        You can only access your own tokens, and only through 
        Basic Authentication.

        http://developer.github.com/v3/oauth/#delete-an-authorization
        """
        raise NotImplementedError

    def scopes(self):
        """Check scopes for a token

        You can only access your own tokens, and only through 
        Basic Authentication.


        http://developer.github.com/v3/oauth/#scopes
        """
        raise NotImplementedError

    def authorize_url(self):
        """Get the URL to authorize a user for an application via the web flow

        You can only access your own tokens, and only through 
        Basic Authentication.


        http://developer.github.com/v3/oauth/#web-application-flow
        """
        raise NotImplementedError
