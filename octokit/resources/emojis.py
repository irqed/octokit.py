# encoding: utf-8

"""Methods for the Emojis API
http://developer.github.com/v3/emojis/
"""

from octokit.resources.base import Resource


class Emojis(Resource):
    """Emojis API resource
    """

    def __init__(self, **kwargs):
        super(Emojis, self).__init__(**kwargs)

    def all(self):
        """List all emojis used on GitHub

        http://developer.github.com/v3/emojis/#emojis
        """
        return self._http.get('emojis')
