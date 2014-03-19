# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class CommitCommentsTestCase(OctokitTestCase):
    """Test case for the commit comments API
    """

    def test_all(self):
        """Get a list of comments for a repo test
        """
        comments = self.hub.commit_comments.all('octocat/Hello-World')
        self.assertEqual(type(comments), list)
        self.assertEqual(comments[0]['body'], 'Great stuff')

    def test_commit(self):
        """Get a list of comments for a commit test
        """
        comments = self.hub.commit_comments.commit('octocat/Hello-World',
                                                   '7a3d89be4b')
        self.assertEqual(type(comments), list)
        self.assertEqual(comments[0]['body'], 'Great stuff')

    def test_comment(self):
        """Get a single comment test
        """
        comment = self.hub.commit_comments.comment('octocat/Hello-World', 1)
        self.assertEqual(type(comment), dict)

    def test_create(self):
        """Create a single comment test
        """
        comment = self.hub.commit_comments.create('octocat/Hello-World',
                                                  '7a3d89be4b',
                                                  'It\'s a trap!')
        self.assertEqual(type(comment), dict)

    def test_update(self):
        """Update a single comment test
        """
        comment = self.hub.commit_comments.update('octocat/Hello-World', 1,
                                                  'It\'s an updated trap!')
        self.assertEqual(type(comment), dict)

    def test_remove(self):
        """Remove a single comment test
        """
        is_deleted = self.hub.commit_comments.remove('octocat/Hello-World', 1)
        self.assertEqual(is_deleted, True)
