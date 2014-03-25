# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class FeedsTestCase(OctokitTestCase):
    """Test case for the feeds API
    """
    def test_all(self):
        """Get links for different feeds test
        """
        feeds = self.hub.feeds.all()
        self.assertIn('timeline_url', feeds)
