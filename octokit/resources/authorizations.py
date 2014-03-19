# encoding: utf-8

"""Methods for the Authorizations API

API for users to manage their own tokens.
You can only access your own tokens, and only through Basic Authentication.

http://developer.github.com/v3/oauth_authorizations/
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

        http://developer.github.com/v3/oauth_authorizations/#list-your-authorizations
        """
        return self._http.get('authorizations')

    def authorization(self, auth_id):
        """Get a single authorization for the authenticated user.

        You can only access your own tokens, and only through
        Basic Authentication.


        http://developer.github.com/v3/oauth_authorizations/#get-a-single-authorization
        """
        return self._http.get('authorizations/%s' % auth_id)

    def create(self, scopes, note, note_url=None, client_id=None,
               client_secret=None):
        """You can create your own tokens, and only through

        You can only access your own tokens, and only through
        Basic Authentication.

        http://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        payload = dict(scopes=scopes, note=note)

        if note_url:
            payload['note_url'] = note_url

        if client_id:
            payload['client_id'] = client_id

        if client_secret:
            payload['client_secret'] = client_secret

        return self._http.post('authorizations', payload=payload)

    def update(self, auth_id, scopes=None, add_scopes=None, remove_scopes=None,
               note=None, note_url=None):
        """Update an authorization for the authenticated user.

        You can only access your own tokens, and only through
        Basic Authentication.

        http://developer.github.com/v3/oauth_authorizations/#update-an-existing-authorization
        http://developer.github.com/v3/oauth/#scopes
        """
        payload = dict()

        if scopes:
            payload['scopes'] = scopes

        if add_scopes:
            payload['add_scopes'] = add_scopes

        if remove_scopes:
            payload['remove_scopes'] = remove_scopes

        if note:
            payload['note'] = note

        if note:
            payload['note'] = note

        return self._http.patch('authorizations/%d' % auth_id, payload=payload)

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
