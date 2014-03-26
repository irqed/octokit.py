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

    def test_gist(self):
        """Get a single gist test
        """
        gist = self.hub.gists.gist(1)
        self.assertIn('description', gist)

    def test_create(self):
        """Create a gist test
        """
        files = {'file1.txt': { 'content': 'String file contents'} }

        gist = self.hub.gists.create(files, True,
                                     'the description for this gist')
        self.assertIn('description', gist)
