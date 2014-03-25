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

    def create(self, repo, path, message, content, branch=None, sha=None,
               author=None, committer=None):
        """Add content to a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#create-a-file
        """
        payload = dict(message=message, content=base64.b64encode(content))
        if branch:
            payload['branch'] = branch

        if sha:
            payload['sha'] = sha

        if author:
            payload['author'] = author

        if committer:
            payload['committer'] = committer

        return self._http.put('repos/%s/contents/%s' % (repo, path),
                              payload=payload)

    def update(self, repo, path, sha, message, content, branch=None,
               author=None, committer=None):
        """Update content in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#update-a-file
        """
        return self.create(repo, path, message, content, branch, sha,
                           author, committer)

    def remove(self, repo, path, sha, message, branch=None,
               author=None, committer=None):
        """Delete content in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/repos/contents/#delete-a-file
        """
        payload = dict(message=message, sha=sha)
        if branch:
            payload['branch'] = branch

        if author:
            payload['author'] = author

        if committer:
            payload['committer'] = committer

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
