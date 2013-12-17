# encoding: utf-8

"""Methods for the Meta API
http://developer.github.com/v3/meta/
"""

from octokit.resources.base import Resource


class Meta(Resource):
    """Meta API resource
    """
    url = '/emojis'

    def __init__(self, **kwargs):
        super(Meta, self).__init__(**kwargs)
