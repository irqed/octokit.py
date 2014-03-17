# encoding: utf-8

import octokit
import unittest


try:
    # For Python 3.3 and later
    from unittest.mock import patch
except ImportError:
    from mock import patch


def fake_request():
    """
    A request() implementation that loads json responses from the filesystem.
    Mock Response object!
    """
    pass


class OctokitTestCase(unittest.TestCase):
    """Base test case for all of the octokit resources.
    """

    _multiprocess_can_split_ = True

    def setUp(self):
        """Patch Requests's request() method and start interrupting requests.
        """
        self.patcher = patch('octokit._http._s.request', fake_request)
        self.patcher.start()

        self.hub = octokit.Octokit()

    def tearDown(self):
        """Stop interrupting requests.
        """
        self.patcher.stop()
