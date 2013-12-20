# encoding: utf-8

"""Methods for the Events API
http://developer.github.com/v3/activity/events/
http://developer.github.com/v3/issues/events/
"""

from octokit.resources.base import Resource

class Events(Resource):
    """Events API resource
    """
    url = '/events'

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def public_events(self):
        """List all public events for GitHub
        http://developer.github.com/v3/activity/events/#list-public-events
        """
        raise NotImplementedError

    def user_events(self):
        """List all user events
        http://developer.github.com/v3/activity/events/#list-events-performed-by-a-user
        """
        raise NotImplementedError

    def user_public_events(self):
        """List public user events
        http://developer.github.com/v3/activity/events/#list-public-events-performed-by-a-user
        """
        raise NotImplementedError

    def received_events(self):
        """List events that a user has received
        http://developer.github.com/v3/activity/events/#list-events-that-a-user-has-received
        """
        raise NotImplementedError

    def received_public_events(self):
        """List public events a user has received
        http://developer.github.com/v3/activity/events/#list-public-events-that-a-user-has-received
        """
        raise NotImplementedError

    def repository_events(self):
        """List events for a repository
        http://developer.github.com/v3/activity/events/#list-repository-events
        """
        raise NotImplementedError

    def repository_network_events(self):
        """List public events for a repository's network
        http://developer.github.com/v3/activity/events/#list-public-events-for-a-network-of-repositories
        """
        raise NotImplementedError

    def organization_events(self):
        """List all events for an organization
        http://developer.github.com/v3/activity/events/#list-events-for-an-organization
        """
        raise NotImplementedError

    def organization_public_events(self):
        """List an organization's public events
        http://developer.github.com/v3/activity/events/#list-public-events-for-an-organization
        """
        raise NotImplementedError

    def repository_issue_events(self):
        """Get all Issue Events for a given Repository
        http://developer.github.com/v3/issues/events/#list-events-for-a-repository
        http://developer.github.com/v3/activity/events/#list-issue-events-for-a-repository
        """
        raise NotImplementedError

    def issue_events(self):
        """List events for an Issue
        http://developer.github.com/v3/issues/events/#list-events-for-an-issue
        """
        raise NotImplementedError

    def issue_event(self):
        """Get information on a single Issue Event
        http://developer.github.com/v3/issues/events/#get-a-single-event
        """
        raise NotImplementedError
