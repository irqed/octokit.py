# encoding: utf-8

from .base import OctokitTestCase
from octokit.errors import OctokitNotFoundError


class ContentsTestCase(OctokitTestCase):
    """Test case for the contents API
    """

    def test_readme(self):
        """Get the default Readme for a repository test
        """
        readme = self.hub.contents.readme('octocat/Hello-World')
        self.assertIn('sha', readme)

    def test_contents(self):
        """Get contents of the file test
        """
        readme = self.hub.contents.contents('octocat/Hello-World', 'readme')
        self.assertIn('sha', readme)

    def test_create(self):
        """Add content to a repository test
        """
        author = dict(name='boba fett', email='boba@fett.me')
        content = self.hub.contents.create('octocat/Hello-World', 'hello.txt',
                                           'my commit message', 'Hello World!',
                                           author=author)

        self.assertIn('commit', content)

    def test_update(self):
        """Update content in a repository test
        """
        author = dict(name='boba fett', email='boba@fett.me')
        content = self.hub.contents.update('octocat/Hello-World',
                                           'hello.txt', '7638417db6',
                                           'my update message',
                                           'Hello World!!!',
                                           author=author)

        self.assertIn('commit', content)

    def test_remove(self):
        """Remove content in a repository test
        """
        author = dict(name='boba fett', email='boba@fett.me')
        content = self.hub.contents.remove('octocat/Hello-World',
                                           'hello.txt', '7638417db6',
                                           'my update message',
                                           'Hello World!!!',
                                           author=author)

        self.assertIn('commit', content)

    def test_archive_link(self):
        """Get an archive link for a repo
        """
        link = self.hub.contents.archive_link('octocat/Hello-World')
        self.assertEqual(type(link), unicode)
