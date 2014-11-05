# encoding: utf-8
import os
import unittest
import warnings

from vcr import VCR
from octokit import Octokit

# Turn off requests warnings about unsecure SSL requests since
# no real requests are happening in tests. Everything is routed to VCR afterall
warnings.simplefilter("ignore")

CASSETTES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              'cassettes')

vcr = VCR(
    record_mode='all',
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
