# encoding: utf-8
import os
import unittest

from vcr import VCR
from octokit import Octokit


CASSETTES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              'cassettes')

vcr = VCR(
    record_mode='new_episodes',
    cassette_library_dir=CASSETTES_PATH,
)


class OctokitTestCase(unittest.TestCase):
    """Base test case for all of the octokit resources.
    """

    _multiprocess_can_split_ = True

    def setUp(self):
        """Setup client for all test cases.
        """
        self.hub = Octokit()
