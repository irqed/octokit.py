# encoding: utf-8

"""Methods for the Commits API
http://developer.github.com/v3/repos/commits/
"""

from datetime import datetime, timedelta
from octokit.resources.base import Resource


class Commits(Resource):
    """Commits API resource
    """
    def __init__(self, **kwargs):
        super(Commits, self).__init__(**kwargs)

    def all(self, repo, sha_or_branch=None, path=None, author=None, since=None, until=None):
        """List commits

        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        if isinstance(since, datetime):
            since = since.isoformat()
        elif since:
            since = datetime.strptime(since, "%Y-%m-%d").isoformat()

        if isinstance(until, datetime):
            until = until.isoformat()
        elif until:
            until = datetime.strptime(until, "%Y-%m-%d").isoformat()

        params = self._get_params(sha=sha_or_branch, path=path, author=author,
                                  since=since, until=until)

        return self._http.get('repos/%s/commits' % repo, params=params)

    def since(self, repo, date, sha_or_branch=None):
        """Get commits after a specified date

        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        return self.all(repo, sha_or_branch, since=date)

    def before(self, repo, date, sha_or_branch=None):
        """Get commits before a specified date

        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        return self.all(repo, sha_or_branch, until=date)

    def on(self, repo, date, sha_or_branch=None):
        """Get commits on a specified date

        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        date = datetime.strptime(date, "%Y-%m-%d")
        end_date = date + timedelta(days=1)
        return self.all(repo, sha_or_branch,
                        since=date, until=end_date)

    def between(self, repo, date, end_date, sha_or_branch=None):
        """Get commits made between two nominated dates

        http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        return self.all(repo, sha_or_branch,
                        since=date, until=end_date)

    def commit(self, repo, sha):
        """Get a single commit

        http://developer.github.com/v3/repos/commits/#get-a-single-commit
        """
        return self._http.get('repos/%s/commits/%s' % (repo, sha))

    def git_commit(self, repo, sha):
        """Get a detailed git commit

        http://developer.github.com/v3/git/commits/#get-a-commit
        """
        return self._http.get('repos/%s/git/commits/%s' % (repo, sha))

    def create(self, repo, message, tree, parents, author=None, committer=None):
        """Create a commit

        http://developer.github.com/v3/git/commits/#create-a-commit
        """
        commit = dict(message=message, tree=tree, parents=parents)

        if author:
            commit['author'] = author

        if committer:
            commit['committer'] = committer

        return self._http.post('repos/%s/git/commits' % repo, payload=commit)

    def compare(self, repo, base, head):
        """Compare two commits

        http://developer.github.com/v3/repos/commits/#compare-two-commits
        """
        return self._http.get('repos/%s/compare/%s...%s' % (repo, base, head))

    def merge(self, repo, base, head, commit_message=None):
        """Merge a branch or sha

        http://developer.github.com/v3/repos/merging/#perform-a-merge
        """
        commit = dict(base=base, head=head)
        if commit_message:
            commit['commit_message'] = commit_message

        return self._http.post('repos/%s/merges' % repo, payload=commit)
