# encoding: utf-8

"""Methods for the Git Data API
http://developer.github.com/v3/git/
"""

from octokit.resources.base import Resource


class Objects(Resource):
    """Objects API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Objects, self).__init__(**kwargs)

    def tree(self):
        """Get a single tree, fetching information about its root-level objects
        http://developer.github.com/v3/git/trees/#get-a-tree
        http://developer.github.com/v3/git/trees/#get-a-tree-recursively
        """
        raise NotImplementedError

    def create_tree(self):
        """Create a tree
        http://developer.github.com/v3/git/trees/#create-a-tree
        """
        raise NotImplementedError

    def blob(self):
        """Get a single blob, fetching its content and encoding
        http://developer.github.com/v3/git/blobs/#get-a-blob
        """
        raise NotImplementedError

    def create_blob(self):
        """Create a blob
        http://developer.github.com/v3/git/blobs/#create-a-blob
        """
        raise NotImplementedError

    def tag(self):
        """Get a tag
        http://developer.github.com/v3/git/tags/#get-a-tag
        """
        raise NotImplementedError

    def create_tag(self):
        """Create a tag

        Requires authenticated client.
        http://developer.github.com/v3/git/tags/#create-a-tag-object
        """
        raise NotImplementedError
