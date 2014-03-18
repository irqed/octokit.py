# encoding: utf-8

from base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class AuthorizationsTestCase(OctokitTestCase):
    """Test case for the authorizations resource.
    """

    def test_all(self):
        """Test collection of authorizations response
        """
        authorizations = self.hub.authorizations.all()
        self.assertEqual(type(authorizations), list)

    def test_authorization(self):
        """Test single authorization response
        """
        authorization = self.hub.authorizations.authorization('auth_id')
        self.assertIn('token', authorization)

    def test_authorization_404(self):
        """Test not found response for a single authorization
        """
        with self.assertRaises(OctokitNotFoundError):
            self.hub.authorizations.authorization('auth_id_404')
