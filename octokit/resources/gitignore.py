# encoding: utf-8

"""Methods for the Gitignore API
http://developer.github.com/v3/gitignore/
"""

from octokit.resources.base import Resource


class Gitignore(Resource):
    """Gitignore API resource
    """
    url = '/gitignore/templates'

    def __init__(self, **kwargs):
        super(Gitignore, self).__init__(**kwargs)

    def get(self, **kwargs):
        lang = kwargs.get('lang')
        if lang:
            return self._http.get(self.url + "/%s" % lang)
        else:
            return self._http.get(self.url)
