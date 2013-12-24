# encoding: utf-8

"""Methods for the Users API
http://developer.github.com/v3/users/
"""

from octokit.resources.base import Resource


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
        return self._get("/users")

    def user(self, user=None):
        """Get a single user

        http://developer.github.com/v3/users/#get-a-single-user
        """
        if user:
            return self._get("/users/%s" % user)
        else:
            return self._get("/user")

    def exchange_code_for_token(self):
        """Retrieve the access_token

        http://developer.github.com/v3/oauth/#web-application-flow
        """
        raise NotImplementedError

    def validate_credentials(self):
        """Validate user username and password
        """
        raise NotImplementedError

    def update_user(self, **user_data):
        """Update the authenticated user

        http://developer.github.com/v3/users/#update-the-authenticated-user
        """
        return self._update("/user", **user_data)

    def followers(self, user=None):
        """Get a user's followers

        http://developer.github.com/v3/users/followers/#list-followers-of-a-user
        """
        if user:
            return self._get("/users/%s/followers" % user)
        else:
            return self._get("/user/followers")

    def following(self, user=None):
        """Get list of users a user is following

        http://developer.github.com/v3/users/followers/#list-users-followed-by-another-user
        """
        if user:
            return self._get("/users/%s/following" % user)
        else:
            return self._get("/user/following")

    def follows(self, target, user=None):
        """Check if you are following a user. Alternatively, check if a given user
        is following a target user.

        Requries an authenticated client.

        http://developer.github.com/v3/users/followers/#check-if-you-are-following-a-user
        http://developer.github.com/v3/users/followers/#check-if-one-user-follows-another
        """
        if user:
            path = "/users/%s/following/%s" % (user, target)
        else:
            path = "/user/following/%s" % target
        return self._http.boolean_from_response("GET", path)

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
