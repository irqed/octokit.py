# encoding: utf-8

"""Methods for the Repo Contents API
http://developer.github.com/v3/repos/contents/
"""

from octokit.resources.base import Resource


class Contents(Resource):
    """Contents API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Contents, self).__init__(**kwargs)

    def readme(self):
        """Receive the default Readme for a repository
        http://developer.github.com/v3/repos/contents/#get-the-readme
        """
        raise NotImplementedError

    def contents(self):
        """Receive a listing of a repository folder or the contents of a file
        http://developer.github.com/v3/repos/contents/#get-contents
        """
        raise NotImplementedError

    def create_contents(self):
        """Add content to a repository
        http://developer.github.com/v3/repos/contents/#create-a-file
        """
        raise NotImplementedError

    def update_contents(self):
        """Update content in a repository
        http://developer.github.com/v3/repos/contents/#update-a-file
        """
        raise NotImplementedError

    def delete_contents(self):
        """Delete content in a repository
        http://developer.github.com/v3/repos/contents/#delete-a-file
        """
        raise NotImplementedError

    def archive_link(self):
        """This method will provide a URL to download a tarball or zipball
        archive for a repository.
        http://developer.github.com/v3/repos/contents/#get-archive-link
        """
        raise NotImplementedError
