# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class GistsTestCase(OctokitTestCase):
    """Test case for the gists API
    """
    def test_all(self):
        """Get all public gists test
        """
        gists = self.hub.gists.all()
        self.assertEqual(type(gists), list)

    def test_user(self):
        """Get all octocat's gists test
        """
        gists = self.hub.gists.user('octocat')
        self.assertEqual(type(gists), list)

    def test_public(self):
        """Get all public gists another way test
        """
        gists = self.hub.gists.public()
        self.assertEqual(type(gists), list)

    def test_starred(self):
        """List the authenticated user’s starred gists test
        """
        gists = self.hub.gists.starred()
        self.assertEqual(type(gists), list)
