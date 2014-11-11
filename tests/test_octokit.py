# encoding: utf-8

from octokit import Octokit, errors

from .base import OctokitTestCase, vcr


class AuthTestCase(OctokitTestCase):
    """Test case for the main Client.
    """

    def test_auth_login_password(self):
        hub = Octokit(login='test', password='test123')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.basic_authenticated, True)

        self.assertEqual(hub.token_authenticated, False)
        self.assertEqual(hub.application_authenticated, False)

        with vcr.use_cassette('auth.yml'):
            user = hub.users('octocat').get()
            self.assertEqual(user['login'], 'octocat')

    def test_auth_token(self):
        hub = Octokit(access_token='so_secret_wow')

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub.token_authenticated, True)

        self.assertEqual(hub.basic_authenticated, False)
        self.assertEqual(hub.application_authenticated, False)

        with vcr.use_cassette('auth.yml'):
            user = hub.users('irqed').get()
            self.assertEqual(user['login'], 'irqed')

    def test_auth_application(self):
        hub = Octokit(
            client_id='so_id_wow',
            client_secret='so_secret_wow'
        )

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.application_authenticated, True)

        self.assertEqual(hub.basic_authenticated, False)
        self.assertEqual(hub.token_authenticated, False)
        self.assertEqual(hub.user_authenticated, False)

        with vcr.use_cassette('auth.yml'):
            user = hub.users('mojombo').get()
            self.assertEqual(user['login'], 'mojombo')


class ErrorsTestCase(OctokitTestCase):
    """Test case for custom Octokit exceptions. Cassette for this test case
    should never be removed since it is fake, no real requests ever made.
    """

    def test_error_bad_request(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(0)
            self.assertRaises(errors.OctokitBadRequestError, resourse.get)

    def test_error_not_found(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(1)
            self.assertRaises(errors.OctokitNotFoundError, resourse.get)

    def test_error_unauthorized(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(2)
            self.assertRaises(errors.OctokitUnauthorizedError, resourse.get)

    def test_error_forbidden(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(3)
            self.assertRaises(errors.OctokitForbiddenError, resourse.get)

    def test_error_not_acceptable(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(4)
            self.assertRaises(errors.OctokitNotAcceptableError, resourse.get)

    def test_error_conflict(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(5)
            self.assertRaises(errors.OctokitConflictError, resourse.get)

    def test_error_unsupported_media_type(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(6)
            self.assertRaises(errors.OctokitUnsupportedMediaTypeError,
                              resourse.get)

    def test_error_unprocessable_entity(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(7)
            self.assertRaises(errors.OctokitUnprocessableEntityError,
                              resourse.get)

    def test_error_client(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(8)
            self.assertRaises(errors.OctokitClientError, resourse.get)

    def test_error_internal_server_error(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(9)
            self.assertRaises(errors.OctokitInternalServerErrorError,
                              resourse.get)

    def test_error_not_implemented(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(10)
            self.assertRaises(errors.OctokitNotImplementedError, resourse.get)

    def test_error_bad_gateway(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(11)
            self.assertRaises(errors.OctokitBadGatewayError, resourse.get)

    def test_error_service_unavailable(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(12)
            self.assertRaises(errors.OctokitServiceUnavailableError,
                              resourse.get)

    def test_error_server_error(self):
        with vcr.use_cassette('errors.yml'):
            resourse = self.hub.nonexisting(13)
            self.assertRaises(errors.OctokitServerError, resourse.get)
