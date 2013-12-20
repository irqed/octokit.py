# encoding: utf-8

"""Methods for the Issue Labels API
http://developer.github.com/v3/issues/labels/
"""

from octokit.resources.base import Resource


class Labels(Resource):
    """Labels API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Labels, self).__init__(**kwargs)

    def labels(self):
        """List available labels for a repository
        http://developer.github.com/v3/issues/labels/#list-all-labels-for-this-repository
        """
        raise NotImplementedError

    def label(self):
        """Get single label for a repository
        http://developer.github.com/v3/issues/labels/#get-a-single-label
        """
        raise NotImplementedError

    def add_label(self):
        """Add a label to a repository
        http://developer.github.com/v3/issues/labels/#create-a-label
        """
        raise NotImplementedError

    def update_label(self):
        """Update a label
        http://developer.github.com/v3/issues/labels/#update-a-label
        """
        raise NotImplementedError

    def delete_label(self):
        """Delete a label from a repository
        http://developer.github.com/v3/issues/labels/#delete-a-label
        """
        raise NotImplementedError

    def remove_label(self):
        """Remove a label from an Issue
        http://developer.github.com/v3/issues/labels/#remove-a-label-from-an-issue
        """
        raise NotImplementedError

    def remove_all_labels(self):
        """Remove all label from an Issue
        http://developer.github.com/v3/issues/labels/#remove-all-labels-from-an-issue
        """
        raise NotImplementedError

    def labels_for_issue(self):
        """List labels for a given issue
        http://developer.github.com/v3/issues/labels/#list-labels-on-an-issue
        """
        raise NotImplementedError

    def add_labels_to_issue(self):
        """Add label(s) to an Issue
        http://developer.github.com/v3/issues/labels/#add-labels-to-an-issue
        """
        raise NotImplementedError

    def replace_all_labels(self):
        """Replace all labels on an Issue
        http://developer.github.com/v3/issues/labels/#replace-all-labels-for-an-issue
        """
        raise NotImplementedError

    def labels_for_milestone(self):
        """Get labels for every issue in a milestone
        http://developer.github.com/v3/issues/labels/#get-labels-for-every-issue-in-a-milestone
        """
        raise NotImplementedError
