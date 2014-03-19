# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class AuthorizationsTestCase(OctokitTestCase):
    """Test case for the authorizations API
    """

    def test_all(self):
        """Get a list of authorizations test
        """
        authorizations = self.hub.authorizations.all()
        self.assertEqual(type(authorizations), list)
        self.assertIn('id', authorizations[0])
        self.assertIn('token', authorizations[0])

    def test_authorization(self):
        """Get a single authorization test
        """
        authorization = self.hub.authorizations.authorization(1)
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_authorization_404(self):
        """Not found response for a single authorization test
        """
        with self.assertRaises(OctokitNotFoundError):
            self.hub.authorizations.authorization(666)

    def test_create(self):
        """Create a new authorization response test
        """
        authorization = self.hub.authorizations.create(['public_repo',], 'test')
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_update(self):
        """Update an existing authorization test
        """
        authorization = self.hub.authorizations.update(1, add_scopes=['repo',])
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_remove(self):
        """Remove an existing authorization test
        """
        is_deleted = self.hub.authorizations.remove(1)
        self.assertEqual(is_deleted, True)
