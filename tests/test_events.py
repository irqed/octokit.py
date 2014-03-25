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
