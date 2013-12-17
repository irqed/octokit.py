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
