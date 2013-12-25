# encoding: utf-8

"""Methods for the Users API
http://developer.github.com/v3/users/
"""

from octokit.resources.base import Resource


class User(Resource):
    """Users API resource, methods to work with authenticatied user
    """
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def info(self):
        """Get the authenticatied user info.

        Requries an authenticated client.
        """
        return self._http.get('user')

    def update(self, user_info):
        """Update the authenticated user.

        Requries an authenticated client.

        http://developer.github.com/v3/users/#update-the-authenticated-user
        """
        return self._http.patch('user', user_info)

    def exchange_code_for_token(self):
        """Retrieve the access_token.

        Requries an authenticated client.

        http://developer.github.com/v3/oauth/#web-application-flow
        """
        raise NotImplementedError

    def validate_credentials(self):
        """Validate user username and password.

        Requries an authenticated client.

        """
        raise NotImplementedError

    def followers(self):
        """Get the authenticated user's followers.

        Requries an authenticated client.

        http://developer.github.com/v3/users/followers/#list-followers-of-a-user
        """
        return self._http.get('user/followers')

    def following(self):
        """Get list of users the authenticated user is following.

        Requries an authenticated client.

        http://developer.github.com/v3/users/followers/#list-users-followed-by-another-user
        """
        return self._http.get('user/following')

    def follows(self, target):
        """Check if you are following a user.

        Requries an authenticated client.

        http://developer.github.com/v3/users/followers/#check-if-you-are-following-a-user
        """
        return self._http.boolean_from_response('GET',
                                                'user/following/%s' % target)

    def follow(self, target):
        """Follow a user

        Requires authenticatied client.

        http://developer.github.com/v3/users/followers/#follow-a-user
        """
        return self._http.boolean_from_response('PUT',
                                                'user/following/%s' % target)

    def unfollow(self, target):
        """Unfollow a user

        Requires authenticated client.

        http://developer.github.com/v3/users/followers/#unfollow-a-user
        """
        return self._http.boolean_from_response('DELETE',
                                                'user/following/%s' % target)

    def starred(self):
        """Get list of repos starred by the authenticated user.

        Requires authenticated client.

        http://developer.github.com/v3/activity/starring/#list-repositories-being-starred
        """
        return self._http.get('user/starred')

    def is_starred(self, repo):
        """Check if you are starring a repo

        http://developer.github.com/v3/activity/starring/#check-if-you-are-starring-a-repository
        """
        return self._http.boolean_from_response('GET',
                                                'user/starred/%s' % repo)

    def key(self, key_id):
        """Get a public key

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#get-a-single-public-key
        """
        return self._http.get('user/keys/%s' % key_id)

    def keys(self):
        """Get list of public keys for the authenticated user.

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#list-your-public-keys
        """
        return self._http.get('user/keys')

    def add_key(self, key_info):
        """Add public key to user account.

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#create-a-public-key
        """
        return self._http.post('user/keys', key_info)

    def update_key(self, key_id, key_info):
        """Update a public key.

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#update-a-public-key
        """
        return self._http.patch('user/keys/%s' % key_id, key_info)

    def remove_key(self, key_id):
        """Remove a public key from user account

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#delete-a-public-key
        """
        return self._http.boolean_from_response('DELETE',
                                                'user/keys/%s' % key_id)

    def emails(self):
        """List email addresses for the authenticated user.

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#list-email-addresses-for-a-user
        """
        return self._http.get('user/emails')

    def add_email(self, emails):
        """Add email address to the authenticated user.

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#add-email-addresses
        """
        return self._http.post('user/emails', emails)

    def remove_email(self, emails):
        """Remove email from the authenticated user.

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#delete-email-addresses
        """
        return self._http.boolean_from_response('DELETE',
                                                'user/emails', payload=emails)

class Users(Resource):
    """Users API resource
    """
    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def all_users(self):
        """List all GitHub users

        This provides a dump of every user, in the order that they signed up
        for GitHub.

        http://developer.github.com/v3/users/#get-all-users
        """
        return self._get('users')

    def user(self, user):
        """Get a single user

        http://developer.github.com/v3/users/#get-a-single-user
        """
        return self._get('users/%s' % user)

    def followers(self, user):
        """Get a user's followers

        http://developer.github.com/v3/users/followers/#list-followers-of-a-user
        """
        return self._get('users/%s/followers' % user)

    def following(self, user):
        """Get list of users a user is following

        http://developer.github.com/v3/users/followers/#list-users-followed-by-another-user
        """
        return self._get('users/%s/following' % user)

    def follows(self, user, target):
        """Check if a given user is following a target user.

        http://developer.github.com/v3/users/followers/#check-if-one-user-follows-another
        """
        path = "/users/%s/following/%s" % (user, target)
        return self._http.boolean_from_response('GET', path)

    def starred(self, user):
        """Get list of repos starred by a user

        http://developer.github.com/v3/activity/starring/#list-repositories-being-starred
        """
        return self._http.get('/users/%s/starred' % user)

    def key(self):
        """Get a public keys

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#get-a-single-public-key
        """
        raise NotImplementedError

    def keys(self, user):
        """Get list of public keys for user

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#list-your-public-keys
        """
        return self._http.get('users/%s/key' % user)

    def subscriptions(self):
        """List repositories being watched by a user

        http://developer.github.com/v3/activity/watching/#list-repositories-being-watched
        """
        raise NotImplementedError
