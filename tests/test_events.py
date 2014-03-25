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
