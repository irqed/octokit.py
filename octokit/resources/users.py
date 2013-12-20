# encoding: utf-8

"""Methods for the Users API
http://developer.github.com/v3/users/
"""

from octokit.resources.base import Resource


class User(Resource):
    """User API resource
    http://developer.github.com/v3/users/#get-the-authenticated-user
    """
    url = '/user'

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def update(self, **kwargs):
        """Update the authenticated user
        http://developer.github.com/v3/users/#update-the-authenticated-user
        """
        return self._http.patch(self.url, **kwargs)


class Users(Resource):
    """Users API resource
    """
    url = '/users'

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def get(self, **kwargs):
        """Get a list if users, or get a single user by login
        """
        login = kwargs.get('login')
        if login:
            return self._http.get(self.url + "/%s" % login)
        else:
            return self._http.get(self.url)

    def all_users(self):
        """List all GitHub users

        This provides a dump of every user, in the order that they signed up
        for GitHub.

        http://developer.github.com/v3/users/#get-all-users
        """
        raise NotImplementedError

    def user(self):
        """Get a single user
        http://developer.github.com/v3/users/#get-a-single-user
        http://developer.github.com/v3/users/#get-the-authenticated-user
        """
        raise NotImplementedError

    def exchange_code_for_token(self):
        """Retrieve the access_token

        http://developer.github.com/v3/oauth/#web-application-flow
        """
        raise NotImplementedError

    def validate_credentials(self):
        """Validate user username and password
        """
        raise NotImplementedError

    def update_user(self):
        """Update the authenticated user

        http://developer.github.com/v3/users/#update-the-authenticated-user
        """
        raise NotImplementedError

    def followers(self):
        """Get a user's followers

        http://developer.github.com/v3/users/followers/#list-followers-of-a-user
        """
        raise NotImplementedError

    def following(self):
        """Get list of users a user is following

        http://developer.github.com/v3/users/followers/#list-users-followed-by-another-user
        """
        raise NotImplementedError

    def follows(self):
        """Check if you are following a user. Alternatively, check if a given user
        is following a target user.

        Requries an authenticated client.

        http://developer.github.com/v3/users/followers/#check-if-you-are-following-a-user
        http://developer.github.com/v3/users/followers/#check-if-one-user-follows-another
        """
        raise NotImplementedError

    def follow(self):
        """Follow a user

        Requires authenticatied client.

        http://developer.github.com/v3/users/followers/#follow-a-user
        """
        raise NotImplementedError

    def unfollow(self):
        """Unfollow a user

        Requires authenticated client.

        http://developer.github.com/v3/users/followers/#unfollow-a-user
        """
        raise NotImplementedError

    def starred(self):
        """Get list of repos starred by a user

        http://developer.github.com/v3/activity/starring/#list-repositories-being-starred
        """
        raise NotImplementedError

    def is_starred(self):
        """Check if you are starring a repo

        http://developer.github.com/v3/activity/starring/#check-if-you-are-starring-a-repository
        """
        raise NotImplementedError

    def key(self):
        """Get a public key

        Note, when using dot notation to retrieve the values, ruby will return
        the hash key for the public keys value instead of the actual value, use
        symbol or key string to retrieve the value. See example.

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#get-a-single-public-key
        """
        raise NotImplementedError

    def keys(self):
        """Get list of public keys for user

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#list-your-public-keys
        """
        raise NotImplementedError

    def add_key(self):
        """Add public key to user account

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#create-a-public-key
        """
        raise NotImplementedError

    def update_key(self):
        """Update a public key

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#update-a-public-key
        """
        raise NotImplementedError

    def remove_key(self):
        """Remove a public key from user account

        Requires authenticated client.

        http://developer.github.com/v3/users/keys/#delete-a-public-key
        """
        raise NotImplementedError

    def emails(self):
        """List email addresses for a user

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#list-email-addresses-for-a-user
        """
        raise NotImplementedError

    def add_email(self):
        """Add email address to user

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#add-email-addresses
        """
        raise NotImplementedError

    def remove_email(self):
        """Remove email from user

        Requires authenticated client.

        http://developer.github.com/v3/users/emails/#delete-email-addresses
        """
        raise NotImplementedError

    def subscriptions(self):
        """List repositories being watched by a user

        http://developer.github.com/v3/activity/watching/#list-repositories-being-watched
        """
        raise NotImplementedError
