# encoding: utf-8

from octokit import Octokit, errors

from .base import OctokitTestCase, vcr


class ClientTestCase(OctokitTestCase):
    """Test case for the main Client.
    """

    def test_auth_login_password(self):
        hub = Octokit(login='test', password='test123')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.basic_authenticated, True)

        self.assertEqual(hub.token_authenticated, False)
        self.assertEqual(hub.application_authenticated, False)

    def test_auth_token(self):
        hub = Octokit(access_token='secret')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.token_authenticated, True)

        self.assertEqual(hub.basic_authenticated, False)
        self.assertEqual(hub.application_authenticated, False)

    def test_auth_application(self):
        hub = Octokit(client_id='id', client_secret='secret')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.application_authenticated, True)

        self.assertEqual(hub.basic_authenticated, False)
        self.assertEqual(hub.token_authenticated, False)
        self.assertEqual(hub.user_authenticated, False)

    def test_error_unauthorized(self):
        with vcr.use_cassette('client.yml'):
            with self.assertRaises(errors.OctokitUnauthorizedError):
                self.hub.authorizations.get()
