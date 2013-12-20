# encoding: utf-8

"""Methods for the Issues Milestones API
http://developer.github.com/v3/issues/milestones/
"""

from octokit.resources.base import Resource


class Milestones(Resource):
    """Milestones API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Milestones, self).__init__(**kwargs)

    def list_milestones(self):
        """List milestones for a repository
        http://developer.github.com/v3/issues/milestones/#list-milestones-for-a-repository
        """
        raise NotImplementedError

    def milestone(self):
        """Get a single milestone for a repository
        http://developer.github.com/v3/issues/milestones/#get-a-single-milestone
        """
        raise NotImplementedError

    def create_milestone(self):
        """Create a milestone for a repository
        http://developer.github.com/v3/issues/milestones/#create-a-milestone
        """
        raise NotImplementedError

    def update_milestone(self):
        """Update a milestone for a repository
        http://developer.github.com/v3/issues/milestones/#update-a-milestone
        """
        raise NotImplementedError

    def delete_milestone(self):
        """Delete a single milestone for a repository
        http://developer.github.com/v3/issues/milestones/#delete-a-milestone
        """
        raise NotImplementedError
