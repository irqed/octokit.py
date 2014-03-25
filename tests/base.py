# encoding: utf-8

import os
import json
import octokit
import unittest

from requests.models import Response
from requests.hooks import dispatch_hook


try:
    # For Python 3.3 and later
    from unittest.mock import patch
except ImportError:
    from mock import patch


try:
    # For Python 3.0 and later
    from urllib.parse import urlparse
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2.X
    from urlparse import urlparse
    from urllib2 import HTTPError


def fake_request(self, method, url, params=None, data=None, headers=None,
                 cookies=None, files=None, auth=None, timeout=None,
                 allow_redirects=True, proxies=None, hooks=None, stream=None,
                 verify=None, cert=None):
    """A request() implementation that loads json responses from the filesystem.
    """
    parsed_url = urlparse(url)
    path = 'tests/fixtures%s_%s.json' % (parsed_url.path, method.lower())
    resource_path = os.path.normpath(path)
    if not os.path.isfile(resource_path):
        resource_path = os.path.normpath('tests/fixtures/404.json')

    resource_file = open(resource_path, 'r')
    response_data = json.loads(resource_file.read())

    response = Response()
    response._content = json.dumps(response_data['body'])
    response.status_code = response_data['status_code']

    if 'headers' in response_data:
        response.headers = response_data['headers']

    if hooks:
        response = dispatch_hook('response', hooks, response)

    return response


class OctokitTestCase(unittest.TestCase):
    """Base test case for all of the octokit resources.
    """

    _multiprocess_can_split_ = True

    def setUp(self):
        """Patch Requests's request() method and start interrupting requests.
        """
        self.patcher = patch('requests.sessions.Session.request', fake_request)
        self.patcher.start()

        self.hub = octokit.Octokit()

    def tearDown(self):
        """Stop interrupting requests.
        """
        self.patcher.stop()
