# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class EmojisTestCase(OctokitTestCase):
    """Test case for the emojis API
    """

    def test_all(self):
        """Get a list of emojis test
        """
        emojis = self.hub.emojis.all()
        self.assertIn('+1', emojis)
