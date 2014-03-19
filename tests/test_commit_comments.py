# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class CommitCommentsTestCase(OctokitTestCase):
    """Test case for the commit comments API
    """

    def test_all(self):
        """Test collection of repo comments response
        """
        comments = self.hub.commit_comments.all('octocat/Hello-World')
        self.assertEqual(type(comments), list)
        self.assertEqual(comments[0]['body'], 'Great stuff')

    def test_commit(self):
        comments = self.hub.commit_comments.commit(self.repo, self.sha)
        self.assertEqual(type(comments), list)

    def test_comment(self):
        comment = self.hub.commit_comments.comment(self.repo, self.comment_id)
        self.assertEqual(type(comment), dict)

    def test_create_remove(self):
        comment = self.hub.commit_comments.create(self.repo, self.sha,
                                                  "It's a trap!")
        self.assertEqual(type(comment), dict)
        self.assertEqual(self.hub.commit_comments.remove(self.repo, comment['id']), True)

    def test_update(self):
        comment = self.hub.commit_comments.create(self.repo, self.sha,
                                                  "It's an updated trap!")
        self.assertEqual(type(comment), dict)
