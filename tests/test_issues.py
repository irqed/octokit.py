# encoding: utf-8

from .base import OctokitTestCase


class IssuesTestCase(OctokitTestCase):
    """Test case for the issues API
    """
    def test_all(self):
        """Get a list all issues for a the authenticated user test
        """
        issues = self.hub.issues.all()
        self.assertEqual(type(issues), list)
        self.assertNotEqual(len(issues), 0)

    def test_user(self):
        """Get a list of all issues across owned and member repositories test
        """
        issues = self.hub.issues.user()
        self.assertEqual(type(issues), list)
        self.assertNotEqual(len(issues), 0)
