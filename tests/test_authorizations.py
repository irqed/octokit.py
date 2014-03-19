# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class AuthorizationsTestCase(OctokitTestCase):
    """Test case for the authorizations resource
    """

    def test_all(self):
        """Test collection of authorizations response
        """
        authorizations = self.hub.authorizations.all()
        self.assertEqual(type(authorizations), list)
        self.assertIn('id', authorizations[0])
        self.assertIn('token', authorizations[0])

    def test_authorization(self):
        """Test single authorization response
        """
        authorization = self.hub.authorizations.authorization(1)
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_authorization_404(self):
        """Test not found response for a single authorization
        """
        with self.assertRaises(OctokitNotFoundError):
            self.hub.authorizations.authorization(666)

    def test_create(self):
        """Test create a new authorization response
        """
        authorization = self.hub.authorizations.create(['public_repo',], 'test')
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_update(self):
        """Test update an existing authorization response
        """
        authorization = self.hub.authorizations.update(1, add_scopes=['repo',])
        self.assertIn('id', authorization)
        self.assertIn('token', authorization)

    def test_remove(self):
        """Test remove an existing authorization response
        """
        is_deleted = self.hub.authorizations.remove(1)
        self.assertEqual(is_deleted, True)
