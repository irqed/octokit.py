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

    def commit_comments(self):
        """List comments for a single commit

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#list-comments-for-a-single-commit
        """
        raise NotImplementedError

    def commit_comment(self):
        """Get a single commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#get-a-single-commit-comment
        """
        raise NotImplementedError

    def create_commit_comment(self):
        """Create a commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#create-a-commit-comment
        """
        raise NotImplementedError

    def update_commit_comment(self):
        """Update a commit comment:

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#update-a-commit-comment
        """
        raise NotImplementedError

    def delete_commit_comment(self):
        """Delete a commit comment

        Requries an authenticated client.

        http://developer.github.com/v3/repos/comments/#delete-a-commit-comment
        """
        raise NotImplementedError
