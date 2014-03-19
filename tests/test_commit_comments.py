# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class CommitCommentsTestCase(OctokitTestCase):
    """Test case for the commit comments API
    """

    def test_all(self):
        """Test all(): get a list of repo comments
        """
        comments = self.hub.commit_comments.all('octocat/Hello-World')
        self.assertEqual(type(comments), list)
        self.assertEqual(comments[0]['body'], 'Great stuff')

    def test_commit(self):
        """Test commit(): get a list of commit comments
        """
        comments = self.hub.commit_comments.commit('octocat/Hello-World',
                                                   '7a3d89be4b')
        self.assertEqual(type(comments), list)
        self.assertEqual(comments[0]['body'], 'Great stuff')

    def test_comment(self):
        """Test comment(): get a single commit comment
        """
        comment = self.hub.commit_comments.comment('octocat/Hello-World', 1)
        self.assertEqual(type(comment), dict)

    def test_create(self):
        """Test create(): create a single commit comment
        """
        comment = self.hub.commit_comments.create('octocat/Hello-World',
                                                  '7a3d89be4b',
                                                  'It\'s a trap!')
        self.assertEqual(type(comment), dict)

    def test_update(self):
        """Test update(): create a single commit comment
        """
        comment = self.hub.commit_comments.update('octocat/Hello-World', 1,
                                                  'It\'s an updated trap!')
        self.assertEqual(type(comment), dict)

    def test_remove(self):
        """Test remove(): remove a single commit comment
        """
        is_deleted = self.hub.commit_comments.remove('octocat/Hello-World', 1)
        self.assertEqual(is_deleted, True)
