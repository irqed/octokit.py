# encoding: utf-8

"""Methods for the Pull Requests API
http://developer.github.com/v3/pulls/
"""

from octokit.resources.base import Resource


class PullRequests(Resource):
    """PullRequests API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(PullRequests, self).__init__(**kwargs)

    def pull_requests(self):
        """List pull requests for a repository

        http://developer.github.com/v3/pulls/#list-pull-requests
        """
        raise NotImplementedError

    def pull_request(self):
        """Get a pull request

        http://developer.github.com/v3/pulls/#get-a-single-pull-request
        """
        raise NotImplementedError

    def create_pull_request(self):
        """Create a pull request

        http://developer.github.com/v3/pulls/#create-a-pull-request
        """
        raise NotImplementedError

    def create_pull_request_for_issue(self):
        """Create a pull request from existing issue

        http://developer.github.com/v3/pulls/#alternative-input
        """
        raise NotImplementedError

    def update_pull_request(self):
        """Update a pull request

        http://developer.github.com/v3/pulls/#update-a-pull-request
        """
        raise NotImplementedError

    def close_pull_request(self):
        """Close a pull request

        http://developer.github.com/v3/pulls/#update-a-pull-request
        """
        raise NotImplementedError

    def pull_request_commits(self):
        """List commits on a pull request

        http://developer.github.com/v3/pulls/#list-commits-on-a-pull-request
        """
        raise NotImplementedError

    def pull_requests_comments(self):
        """List pull request comments for a repository

        By default, Review Comments are ordered by ascending ID.

        http://developer.github.com/v3/pulls/comments/#list-comments-in-a-repository
        """
        raise NotImplementedError

    def pull_request_comments(self):
        """List comments on a pull request

        http://developer.github.com/v3/pulls/#list-comments-on-a-pull-request
        """
        raise NotImplementedError

    def pull_request_comment(self):
        """Get a pull request comment

        http://developer.github.com/v3/pulls/comments/#get-a-single-comment
        """
        raise NotImplementedError

    def create_pull_request_comment(self):
        """Create a pull request comment

        http://developer.github.com/v3/pulls/comments/#create-a-comment
        """
        raise NotImplementedError

    def create_pull_request_comment_reply(self):
        """Create reply to a pull request comment

        http://developer.github.com/v3/pulls/comments/#create-a-comment
        """
        raise NotImplementedError

    def update_pull_request_comment(self):
        """Update pull request comment

        http://developer.github.com/v3/pulls/comments/#edit-a-comment
        """
        raise NotImplementedError

    def delete_pull_request_comment(self):
        """Delete pull request comment

        http://developer.github.com/v3/pulls/comments/#delete-a-comment
        """
        raise NotImplementedError

    def pull_request_files(self):
        """List files on a pull request

        http://developer.github.com/v3/pulls/#list-pull-requests-files
        """
        raise NotImplementedError

    def merge_pull_request(self):
        """Merge a pull request

        http://developer.github.com/v3/pulls/#merge-a-pull-request-merge-buttontrade
        """
        raise NotImplementedError

    def is_pull_merged(self):
        """Check pull request merge status

        http://developer.github.com/v3/pulls/#get-if-a-pull-request-has-been-merged
        """
        raise NotImplementedError
