# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class CommitsTestCase(OctokitTestCase):
    """Test case for the commits API
    """

    def test_all(self):
        """Get a list of all commits test
        """
        commits = self.hub.commits.all('octocat/Hello-World')
        self.assertEqual(type(commits), list)

    def test_since(self):
        """Get a list of all commits since the specified date test
        """
        commits = self.hub.commits.since('octocat/Hello-World', '2011-04-13')
        self.assertEqual(type(commits), list)
        self.assertNotEqual(len(commits), 0)

    def test_before(self):
        """Get a list of all commits before the specified date test
        """
        commits = self.hub.commits.before('octocat/Hello-World', '2011-04-15')
        self.assertEqual(type(commits), list)
        self.assertNotEqual(len(commits), 0)

    def test_on(self):
        """Get a list of all commits on the specified date test
        """
        commits = self.hub.commits.on('octocat/Hello-World', '2011-04-14')
        self.assertEqual(type(commits), list)
        self.assertNotEqual(len(commits), 0)

    def test_between(self):
        """Get a list of all commits between two dates test
        """
        commits = self.hub.commits.between('octocat/Hello-World',
                                           '2011-04-13', '2011-04-15')
        self.assertEqual(type(commits), list)
        self.assertNotEqual(len(commits), 0)

    def test_commit(self):
        """Get a single commit test
        """
        commit = self.hub.commits.commit('octocat/Hello-World', '7a3d89be4b')
        self.assertEqual(type(commit), dict)

    def test_git_commit(self):
        """Get a detailed git commit test
        """
        commit = self.hub.commits.git_commit('octocat/Hello-World', '7a3d89be4b')
        self.assertEqual(type(commit), dict)

    def test_create_commit(self):
        """Create a commit test
        """
        pass

    def test_compare(self):
        """Compare two commits test
        """
        pass

    def test_merge(self):
        """Merge a branch or sha test
        """
        pass
