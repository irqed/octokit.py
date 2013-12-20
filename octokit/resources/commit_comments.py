# encoding: utf-8

"""Methods for the Commit Comments API
http://developer.github.com/v3/repos/comments/
"""


class CommitComments(Resource):
    """CommitComments API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(CommitComments, self).__init__(**kwargs)

    def list_commit_comments(self):
        """List all commit comments
        http://developer.github.com/v3/repos/comments/#list-commit-comments-for-a-repository
        """
        raise NotImplementedError

    def commit_comments(self):
        """List comments for a single commit
        http://developer.github.com/v3/repos/comments/#list-comments-for-a-single-commit
        """
        raise NotImplementedError

    def commit_comment(self):
        """Get a single commit comment
        http://developer.github.com/v3/repos/comments/#get-a-single-commit-comment
        """
        raise NotImplementedError

    def create_commit_comment(self):
        """Create a commit comment
        http://developer.github.com/v3/repos/comments/#create-a-commit-comment
        """
        raise NotImplementedError

    def update_commit_comment(self):
        """Update a commit comment:
        http://developer.github.com/v3/repos/comments/#update-a-commit-comment
        """
        raise NotImplementedError

    def delete_commit_comment(self):
        """Delete a commit comment
        http://developer.github.com/v3/repos/comments/#delete-a-commit-comment
        """
        raise NotImplementedError
