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

    def gists(self):
        """List gists for a user or all public gists
        http://developer.github.com/v3/gists/#list-gists
        """

    def public_gists(self):
        """List public gists
        http://developer.github.com/v3/gists/#list-gists
        """

    def starred_gists(self):
        """List the authenticated user’s starred gists
        http://developer.github.com/v3/gists/#list-gists
        """

    def gist(self):
        """Get a single gist
        http://developer.github.com/v3/gists/#get-a-single-gist
        """

    def create_gist(self):
        """Create a gist
        http://developer.github.com/v3/gists/#create-a-gist
        """

    def edit_gist(self):
        """Edit a gist
        http://developer.github.com/v3/gists/#edit-a-gist
        """

    def star_gist(self):
        """Star a gist
        http://developer.github.com/v3/gists/#star-a-gist
        """

    def unstar_gist(self):
        """Unstar a gist
        http://developer.github.com/v3/gists/#unstar-a-gist
        """

    def gist_starred(self):
        """Check if a gist is starred
        http://developer.github.com/v3/gists/#check-if-a-gist-is-starred
        """

    def fork_gist(self):
        """Fork a gist
        http://developer.github.com/v3/gists/#fork-a-gist
        """

    def delete_gist(self):
        """Delete a gist
        http://developer.github.com/v3/gists/#delete-a-gist
        """

    def gist_comments(self):
        """List gist comments
        http://developer.github.com/v3/gists/comments/#list-comments-on-a-gist
        """

    def gist_comment(self):
        """Get gist comment
        http://developer.github.com/v3/gists/comments/#get-a-single-comment
        """

    def create_gist_comment(self):
        """Create gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#create-a-comment
        """

    def update_gist_comment(self):
        """Update gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#edit-a-comment
        """

    def delete_gist_comment(self):
        """Delete gist comment

        Requires authenticated client.
        http://developer.github.com/v3/gists/comments/#delete-a-comment
        """
