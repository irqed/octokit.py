# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class GitignoreTestCase(OctokitTestCase):
    """Test case for the gitignore API
    """
    def test_templates(self):
        """Get a list of gitignore templates test
        """
        templates = self.hub.gitignore.templates()
        self.assertEqual(type(templates), list)
        self.assertNotEqual(len(templates), 0)

    def test_template(self):
        """Get gitignore template for C test
        """
        template = self.hub.gitignore.template('C')
        self.assertEqual(type(template), dict)
