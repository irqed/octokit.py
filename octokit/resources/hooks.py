# encoding: utf-8

"""Methods for the Hooks API
http://developer.github.com/v3/repos/hooks/
"""

from octokit.resources.base import Resource


class Hooks(Resource):
    """Hooks API resource
    """
    url = '/hooks'

    def __init__(self, **kwargs):
        super(Hooks, self).__init__(**kwargs)

    def available_hooks(self):
        """List all Service Hooks supported by GitHub
        http://developer.github.com/v3/repos/hooks/#services
        """
        raise NotImplementedError
