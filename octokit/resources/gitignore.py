# encoding: utf-8

"""Methods for the Gitignore API
http://developer.github.com/v3/gitignore/
"""

from octokit.resources.base import Resource


class Gitignore(Resource):
    """Gitignore API resource
    """
    def __init__(self, **kwargs):
        super(Gitignore, self).__init__(**kwargs)

    def templates(self):
        """Listing available gitignore templates

        http://developer.github.com/v3/gitignore/#listing-available-templates
        """
        return self._http.get('gitignore/templates')

    def template(self, name):
        """Get a gitignore template

        Use the raw {http://developer.github.com/v3/media/ media type} to get
        the raw contents.
        http://developer.github.com/v3/gitignore/#get-a-single-template
        """
        return self._http.get('gitignore/templates/%s' % name)
