# encoding: utf-8

"""Methods for the Markdown API
http://developer.github.com/v3/markdown/
"""

from octokit.resources.base import Resource


class Markdown(Resource):
    """Markdown API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Markdown, self).__init__(**kwargs)

    def markdown(self):
        """Render an arbitrary Markdown document
        http://developer.github.com/v3/markdown/#render-an-arbitrary-markdown-document
        """
        raise NotImplementedError
