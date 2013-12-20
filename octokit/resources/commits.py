# encoding: utf-8

"""Methods for the Commits API
http://developer.github.com/v3/repos/commits/
"""

from octokit.resources.base import Resource


class Commits(Resource):
    """Commits API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Commits, self).__init__(**kwargs)

    def commits(self):
        """List commits
        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        raise NotImplementedError

    def commits_since(self):
        """Get commits after a specified date
        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        raise NotImplementedError

    def commits_before(self):
        """Get commits before a specified date
        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        raise NotImplementedError

    def commits_on(self):
        """Get commits on a specified date
        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        raise NotImplementedError

    def commits_between(self):
        """Get commits made between two nominated dates
        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        raise NotImplementedError

    def commit(self):
        """Get a single commit
        http://developer.github.com/v3/repos/commits/#get-a-single-commit
        """
        raise NotImplementedError

    def git_commit(self):
        """Get a detailed git commit
        http://developer.github.com/v3/git/commits/#get-a-commit
        """
        raise NotImplementedError

    def create_commit(self):
        """Create a commit
        http://developer.github.com/v3/git/commits/#create-a-commit
        """
        raise NotImplementedError

    def compare(self):
        """Compare two commits
        http://developer.github.com/v3/repos/commits/#compare-two-commits
        """
        raise NotImplementedError

    def merge(self):
        """Merge a branch or sha
        http://developer.github.com/v3/repos/merging/#perform-a-merge
        """
        raise NotImplementedError
