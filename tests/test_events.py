# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class EventsTestCase(OctokitTestCase):
    """Test case for the events API
    """

    def test_public(self):
        """Get a list of public events
        """
        events = self.hub.events.public()
        self.assertEqual(type(events), list)

    def test_performed_by(self):
        """Get a list of events performed by octocat test
        """
        events = self.hub.events.performed_by('octocat')
        self.assertEqual(type(events), list)

    def test_received_by(self):
        """Get a list of events performed by octocat test
        """
        events = self.hub.events.received_by('octocat')
        self.assertEqual(type(events), list)

    def test_repository(self):
        """Get a list of events for repository test
        """
        events = self.hub.events.repository('octocat/Hello-World')
        self.assertEqual(type(events), list)

    def test_repository_network(self):
        """Get a list of events for repository network test
        """
        events = self.hub.events.repository('octocat/Hello-World', True)
        self.assertEqual(type(events), list)

    def test_organization(self):
        """Get a list of event for organization test
        """
        events = self.hub.events.organization('octocats')
        self.assertEqual(type(events), list)

    def test_user_organization(self):
        """Get user's organization dashboard test
        """
        events = self.hub.events.organization('octocats', 'octocat')
        self.assertEqual(type(events), list)

    def test_issues(self):
        """Get a list of events for repository issues test
        """
        events = self.hub.events.issues('octocat/Hello-World')
        self.assertEqual(type(events), list)

    def test_issue(self):
        """Get a list of events for single issues test
        """
        events = self.hub.events.issue('octocat/Hello-World', 1)
        self.assertEqual(type(events), list)

    def test_event(self):
        """GGet information on a single issue event test
        """
        event = self.hub.events.event('octocat/Hello-World', 1)
        self.assertIn('actor', event)
