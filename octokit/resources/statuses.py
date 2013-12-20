# encoding: utf-8

"""Methods for the Commit Statuses API
http://developer.github.com/v3/repos/statuses/
"""

from octokit.resources.base import Resource


class Statuses(Resource):
    """Statuses API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Statuses, self).__init__(**kwargs)

    def statuses(self):
        """List all statuses for a given commit

        http://developer.github.com/v3/repos/statuses/#list-statuses-for-a-specific-ref
        """
        raise NotImplementedError

    def create_status(self):
        """Create status for a commit

        http://developer.github.com/v3/repos/statuses/#create-a-status
        """
        raise NotImplementedError
