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

    def gitignore_templates(self):
        """Listing available gitignore templates

        http://developer.github.com/v3/gitignore/#listing-available-templates
        """
        raise NotImplementedError

    def gitignore_template(self):
        """Get a gitignore template

        Use the raw {http://developer.github.com/v3/media/ media type} to get
        the raw contents.
        http://developer.github.com/v3/gitignore/#get-a-single-template
        """
        raise NotImplementedError
