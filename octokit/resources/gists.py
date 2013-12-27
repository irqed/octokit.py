# encoding: utf-8

"""Methods for the Gists API
http://developer.github.com/v3/gists/
"""

from octokit.resources.base import Resource


class Gists(Resource):
    """Gists API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Gists, self).__init__(**kwargs)

    def all(self, user=None):
        """List gists for a user or all public gists
        http://developer.github.com/v3/gists/#list-gists
        """
        if user:
            path = 'users/%s/gists' % user
        else:
            path = 'gists'
        return self._http.get(path)

    def public(self):
        """List public gists
        http://developer.github.com/v3/gists/#list-gists
        """
        return self._http.get('gists/public')

    def starred_gists(self):
        """List the authenticated user’s starred gists
        http://developer.github.com/v3/gists/#list-gists
        """
        raise NotImplementedError

    def gist(self):
        """Get a single gist
        http://developer.github.com/v3/gists/#get-a-single-gist
        """
        raise NotImplementedError

    def create_gist(self):
        """Create a gist
        http://developer.github.com/v3/gists/#create-a-gist
        """
        raise NotImplementedError

    def edit_gist(self):
        """Edit a gist
        http://developer.github.com/v3/gists/#edit-a-gist
        """
        raise NotImplementedError

    def star_gist(self):
        """Star a gist
        http://developer.github.com/v3/gists/#star-a-gist
        """
        raise NotImplementedError

    def unstar_gist(self):
        """Unstar a gist
        http://developer.github.com/v3/gists/#unstar-a-gist
        """
        raise NotImplementedError

    def gist_starred(self):
        """Check if a gist is starred
        http://developer.github.com/v3/gists/#check-if-a-gist-is-starred
        """
        raise NotImplementedError

    def fork_gist(self):
        """Fork a gist
        http://developer.github.com/v3/gists/#fork-a-gist
        """
        raise NotImplementedError

    def delete_gist(self):
        """Delete a gist
        http://developer.github.com/v3/gists/#delete-a-gist
        """
        raise NotImplementedError

    def gist_comments(self):
        """List gist comments
        http://developer.github.com/v3/gists/comments/#list-comments-on-a-gist
        """
        raise NotImplementedError

    def gist_comment(self):
        """Get gist comment
        http://developer.github.com/v3/gists/comments/#get-a-single-comment
        """
        raise NotImplementedError

    def create_gist_comment(self):
        """Create gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#create-a-comment
        """
        raise NotImplementedError

    def update_gist_comment(self):
        """Update gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#edit-a-comment
        """
        raise NotImplementedError

    def delete_gist_comment(self):
        """Delete gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#delete-a-comment
        """
        raise NotImplementedError
