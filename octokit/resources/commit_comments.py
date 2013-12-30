# encoding: utf-8

"""Methods for the Commit Comments API
http://developer.github.com/v3/repos/comments/
"""

from octokit.resources.base import Resource


class CommitComments(Resource):
    """CommitComments API resource
    """
    def __init__(self, **kwargs):
        super(CommitComments, self).__init__(**kwargs)

    def all(self, repo):
        """List all commit comments

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#list-commit-comments-for-a-repository
        """
        return self._http.get('repos/%s/comments' % repo)

    def commit(self, repo, sha):
        """List comments for a single commit

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#list-comments-for-a-single-commit
        """
        return self._http.get('repos/%s/commits/%s/comments' % (repo, sha))

    def comment(self, repo, comment_id):
        """Get a single commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#get-a-single-commit-comment
        """
        return self._http.get('repos/%s/comments/%s' % (repo, comment_id))

    def create(self, repo, sha, body, path=None, line=None, position=None):
        """Create a commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#create-a-commit-comment
        """
        comment = dict(body=body, commit_id=sha, path=path, line=line,
                       position=position)
        return self._http.post('repos/%s/commits/%s/comments' % (repo, sha),
                               payload=comment)

    def update(self, repo, comment_id, body):
        """Update a commit comment:

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#update-a-commit-comment
        """
        return self._http.patch('repos/%s/comments/%s' % (repo, comment_id),
                                payload=dict(body=body))

    def remove(self, repo, comment_id):
        """Delete a commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#delete-a-commit-comment
        """
        path = 'repos/%s/comments/%s' % (repo, comment_id)
        return self._http.boolean_from_response('DELETE', path)
