# encoding: utf-8

"""Methods for the Issues API
http://developer.github.com/v3/issues/
"""

from octokit.resources.base import Resource


class Issues(Resource):
    """Issues API resource
    """
    url = '/issues'

    def __init__(self, **kwargs):
        super(Issues, self).__init__(**kwargs)

    def list_issues(self):
        """List issues for a the authenticated user or repository
        http://developer.github.com/v3/issues/#list-issues-for-a-repository
        http://developer.github.com/v3/issues/#list-issues
        """
        raise NotImplementedError

    def user_issues(self):
        """List all issues across owned and member repositories for
        the authenticated user

        http://developer.github.com/v3/issues/#list-issues
        """
        raise NotImplementedError

    def org_issues(self):
        """List all issues for a given organization for the authenticated user
        http://developer.github.com/v3/issues/#list-issues
        """
        raise NotImplementedError

    def create_issue(self):
        """Create an issue for a repository
        http://developer.github.com/v3/issues/#create-an-issue
        """
        raise NotImplementedError

    def issue(self):
        """Get a single issue from a repository
        http://developer.github.com/v3/issues/#get-a-single-issue
        """
        raise NotImplementedError

    def close_issue(self):
        """Close an issue
        http://developer.github.com/v3/issues/#edit-an-issue
        """
        raise NotImplementedError

    def reopen_issue(self):
        """Reopen an issue
        http://developer.github.com/v3/issues/#edit-an-issue
        """
        raise NotImplementedError

    def update_issue(self):
        """Update an issue
        http://developer.github.com/v3/issues/#edit-an-issue
        """
        raise NotImplementedError

    def issues_comments(self):
        """Get all comments attached to issues for the repository
        http://developer.github.com/v3/issues/comments/#list-comments-in-a-repository
        """
        raise NotImplementedError

    def issue_comments(self):
        """Get all comments attached to an issue
        http://developer.github.com/v3/issues/comments/#list-comments-on-an-issue
        """
        raise NotImplementedError

    def issue_comment(self):
        """Add a comment to an issue
        http://developer.github.com/v3/issues/comments/#create-a-comment
        """
        raise NotImplementedError

    def add_comment(self):
        """Add a comment to an issue
        http://developer.github.com/v3/issues/comments/#create-a-comment
        """
        raise NotImplementedError

    def update_comment(self):
        """Update a single comment on an issue
        http://developer.github.com/v3/issues/comments/#edit-a-comment
        """
        raise NotImplementedError

    def delete_comment(self):
        """Delete a single comment
        http://developer.github.com/v3/issues/comments/#delete-a-comment
        """
        raise NotImplementedError

