# encoding: utf-8

from octokit import Octokit

from .base import OctokitTestCase, vcr


class ClientTestCase(OctokitTestCase):
    """Test case for the authorizations API
    """

    def test_auth_login_password(self):
        hub = Octokit(login='test', password='test123')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.basic_authenticated, True)

    def test_auth_token(self):
        hub = Octokit(access_token='secret')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.token_authenticated, True)

    def test_auth_application(self):
        hub = Octokit(client_id='id', client_secret='secret')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.application_authenticated, True)
