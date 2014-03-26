# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class IssuesTestCase(OctokitTestCase):
    """Test case for the issues API
    """
    def test_all(self):
        """Get a list of all user issues test
        """
        issues = self.hub.issues.all()
        self.assertEqual(type(issues), list)
        self.assertNotEqual(len(issues), 0)
