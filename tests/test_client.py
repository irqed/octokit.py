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

    def test_resource(self):
        with vcr.use_cassette('client.yml'):
            user = self.hub.users('irqed').get()
            self.assertEqual(user['login'], 'irqed')


class ErrorsTestCase(OctokitTestCase):
    """Test case for custom Octokit exceptions.
    """

    def test_error_bad_request(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitBadRequestError):
                self.hub.nonexisting(0).get()

    def test_error_not_found(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitNotFoundError):
                self.hub.nonexisting(1).get()

    def test_error_unauthorized(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitUnauthorizedError):
                self.hub.nonexisting(2).get()

    def test_error_forbidden(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitForbiddenError):
                self.hub.nonexisting(3).get()

    def test_error_not_acceptable(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitNotAcceptableError):
                self.hub.nonexisting(4).get()

    def test_error_conflict(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitConflictError):
                self.hub.nonexisting(5).get()

    def test_error_unsupported_media_type(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitUnsupportedMediaTypeError):
                self.hub.nonexisting(6).get()

    def test_error_unprocessable_entity(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitUnprocessableEntityError):
                self.hub.nonexisting(7).get()

    def test_error_client(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitClientError):
                self.hub.nonexisting(8).get()

    def test_error_internal_server_error(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitInternalServerErrorError):
                self.hub.nonexisting(9).get()

    def test_error_not_implemented(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitNotImplementedError):
                self.hub.nonexisting(10).get()

    def test_error_bad_gateway(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitBadGatewayError):
                self.hub.nonexisting(11).get()

    def test_error_service_unavailable(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitServiceUnavailableError):
                self.hub.nonexisting(12).get()

    def test_error_server_error(self):
        with vcr.use_cassette('errors.yml', record_mode='once'):
            with self.assertRaises(errors.OctokitServerError):
                self.hub.nonexisting(13).get()
