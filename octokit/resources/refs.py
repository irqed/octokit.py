# encoding: utf-8

"""Methods for References for Git Data API
http://developer.github.com/v3/git/refs/
"""

from octokit.resources.base import Resource


class Refs(Resource):
    """Refs API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Refs, self).__init__(**kwargs)

    def refs(self):
        """List all refs for a given user and repo

        http://developer.github.com/v3/git/refs/#get-all-references
        """

    def ref(self):
        """Fetch a given reference

        http://developer.github.com/v3/git/refs/#get-a-reference
        """

    def create_ref(self):
        """Create a reference

        http://developer.github.com/v3/git/refs/#create-a-reference
        """

    def update_ref(self):
        """Update a reference

        http://developer.github.com/v3/git/refs/#update-a-reference
        """

    def update_branch(self):
        """Update a branch

        http://developer.github.com/v3/git/refs/#update-a-reference
        """

    def delete_branch(self):
        """Delete a single branch

        http://developer.github.com/v3/git/refs/#delete-a-reference
        """

    def delete_ref(self):
        """Delete a single reference

        http://developer.github.com/v3/git/refs/#delete-a-reference
        """
