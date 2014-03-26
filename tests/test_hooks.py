# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class GitignoreTestCase(OctokitTestCase):
    """Test case for the gitignore API
    """
    def test_available(self):
        """Get a list of available hooks test
        """
        hooks = self.hub.hooks.available()
        self.assertEqual(type(hooks), list)
        self.assertNotEqual(len(hooks), 0)
