# encoding: utf-8

"""Methods for the Emojis API
http://developer.github.com/v3/emojis/
"""

from octokit.resources.base import Resource


class Emojis(Resource):
    """Emojis API resource
    """
    url = '/emojis'

    def __init__(self, **kwargs):
        super(Emojis, self).__init__(**kwargs)
