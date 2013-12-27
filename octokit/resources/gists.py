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

    def starred(self):
        """List the authenticated user’s starred gists

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#list-gists
        """

        return self._http.get('gists/starred')

    def gist(self, gist_id):
        """Get a single gist
        http://developer.github.com/v3/gists/#get-a-single-gist
        """
        return self._http.get('gists/%s' % gist_id)

    def create(self, gist):
        """Create a gist

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#create-a-gist
        """
        return self._http.post('gists', gist)

    def edit(self, gist_id, gist):
        """Edit a gist

        Requries an authenticated client.

        NOTE: All files from the previous version of the
        gist are carried over by default if not included in the hash. Deletes
        can be performed by including the filename with a null hash.

        http://developer.github.com/v3/gists/#edit-a-gist
        """
        return self._http.patch('gists/%s' % gist_id, gist)

    def remove(self, gist_id):
        """Delete a gist

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#delete-a-gist
        """
        return self._http.boolean_from_response('DELETE',
                                                'gists/%s' % gist_id)

    def star(self, gist_id):
        """Star a gist

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#star-a-gist
        """
        return self._http.boolean_from_response('PUT',
                                                'gists/%s/star' % gist_id)

    def unstar(self, gist_id):
        """Unstar a gist

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#unstar-a-gist
        """
        return self._http.boolean_from_response('DELETE',
                                                'gists/%s/star' % gist_id)

    def is_starred(self, gist_id):
        """Check if a gist is starred

        Requries an authenticated client.

        http://developer.github.com/v3/gists/#check-if-a-gist-is-starred
        """
        return self._http.boolean_from_response('GET',
                                                'gists/%s/star' % gist_id)

    def fork(self, gist_id):
        """Fork a gist

        http://developer.github.com/v3/gists/#fork-a-gist
        """
        return self._http.post('gists/%s/forks' % gist_id)

    def comments(self, gist_id):
        """List gist comments

        http://developer.github.com/v3/gists/comments/#list-comments-on-a-gist
        """
        return self._http.get('gists/%s/comments' % gist_id)

    def comment(self, gist_id, gist_comment_id):
        """Get gist comment

        http://developer.github.com/v3/gists/comments/#get-a-single-comment
        """
        path = 'gists/%s/comments/%s' % (gist_id, gist_comment_id)
        return self._http.get(path)

    def create_comment(self, gist_id, text):
        """Create gist comment

        Requires authenticated client.

        http://developer.github.com/v3/gists/comments/#create-a-comment
        """
        path = 'gists/%s/comments' % gist_id
        return self._http.post(path, dict(body=text))

    def edit_comment(self, gist_id, gist_comment_id, text):
        """Update gist comment

        Requires authenticated client.

        http://developer.github.com/v3/gists/comments/#edit-a-comment
        """
        path = 'gists/%s/comments/%s' % (gist_id, gist_comment_id)
        return self._http.patch(path, dict(body=text))

    def remove_comment(self, gist_id, gist_comment_id):
        """Delete gist comment

        Requires authenticated client.

        http://developer.github.com/v3/gists/comments/#delete-a-comment
        """
        path = 'gists/%s/comments/%s' % (gist_id, gist_comment_id)
        return self._http.boolean_from_response('DELETE', path)
