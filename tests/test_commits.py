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

    def test_create(self):
        """Create a commit test
        """
        author = dict(name='boba fett', email='boba@fett.me',
                      date='2008-07-09T16:13:30+12:00')
        commit = self.hub.commits.create('octocat/Hello-World',
                                         'my commit message',
                                         '827efc6d56897b048c772eb4087f854f46256132',
                                         ['7d1b31e74ee336d15cbd21741bc88a537ed063a0',],
                                         author=author)
        self.assertEqual(type(commit), dict)

    def test_compare(self):
        """Compare two commits test
        """
        result = self.hub.commits.compare('octocat/Hello-World',
                                          'octocat:master', 'boba:feature')
        self.assertIn('base_commit', result)

    def test_merge(self):
        """Merge a branch or sha test
        """
        result = self.hub.commits.merge('octocat/Hello-World',
                                          'master', 'feature',
                                          'Such merge! Wow!')
        self.assertIn('sha', result)
