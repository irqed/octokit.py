# encoding: utf-8

"""Methods for the Repo Contents API

http://developer.github.com/v3/repos/contents/
"""

import base64

from octokit.resources.base import Resource


class Contents(Resource):
    """Contents API resource
    """
    def __init__(self, **kwargs):
        super(Contents, self).__init__(**kwargs)

    def readme(self, repo, ref='master'):
        """Receive the default Readme for a repository

        http://developer.github.com/v3/repos/contents/#get-the-readme
        """
        params = self._get_params(ref=ref)
        return self._http.get('repos/%s/readme' % repo, params=params)

    def contents(self, repo, path=None, ref='master'):
        """Receive a listing of a repository folder or the contents of a file

        http://developer.github.com/v3/repos/contents/#get-contents
        """
        params = self._get_params(ref=ref)
        if path:
            path = 'repos/%s/contents/%s' % (repo, path)
        else:
            path = 'repos/%s/contents' % repo
        return self._http.get(path, params=params)

    def create_contents(self, repo, path, message, content=None, branch='master', sha=None):
        """Add content to a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#create-a-file
        """
        payload = self._get_params(message=message, branch=branch, sha=sha,
                                   content=base64.b64encode(content))
        return self._http.put('repos/%s/contents/%s' % (repo, path),
                              payload=payload)

    def update_contents(self, repo, path, message, content, sha, branch='master'):
        """Update content in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#update-a-file
        """
        return self.create_contents(repo, path, message, content, branch, sha)

    def remove_contents(self, repo, path, message, sha, branch='master'):
        """Delete content in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#delete-a-file
        """
        payload = self._get_params(message=message, sha=sha, branch=branch)
        return self._http.delete('repos/%s/contents/%s' % (repo, path),
                                 payload=payload)

    def archive_link(self, repo, format='tarball', ref='master'):
        """This method will provide a URL to download a tarball or zipball
        archive for a repository.

        http://developer.github.com/v3/repos/contents/#get-archive-link
        """
        self._http.head('repos/%s/%s/%s' % (repo, format, ref),
                        allow_redirects=False)
        return self._http.last_response.headers['Location']
