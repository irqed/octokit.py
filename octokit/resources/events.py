# encoding: utf-8

"""Methods for the Events API

http://developer.github.com/v3/activity/events/
http://developer.github.com/v3/issues/events/
"""

from octokit.resources.base import Resource

class Events(Resource):
    """Events API resource
    """
    def __init__(self, **kwargs):
        super(Events, self).__init__(**kwargs)

    def public(self):
        """List all public events for GitHub

        http://developer.github.com/v3/activity/events/#list-public-events
        """
        return self._http.get('events')

    def performed_by(self, user, public=False):
        """List all user events

        http://developer.github.com/v3/activity/events/#list-events-performed-by-a-user
        http://developer.github.com/v3/activity/events/#list-public-events-performed-by-a-user
        """
        path = 'users/%s/events/public' if public else 'users/%s/events'
        return self._http.get(path % user)

    def received_by(self, user, public=False):
        """List events that a user has received

        http://developer.github.com/v3/activity/events/#list-events-that-a-user-has-received
        http://developer.github.com/v3/activity/events/#list-public-events-that-a-user-has-received
        """
        path = 'users/%s/received_events/public' if public else 'users/%s/received_events'
        return self._http.get(path % user)

    def repository(self, repo, network=False):
        """List events for a repository

        http://developer.github.com/v3/activity/events/#list-repository-events
        http://developer.github.com/v3/activity/events/#list-public-events-for-a-network-of-repositories
        """
        path = 'networks/%s/events' if network else 'repos/%s/events'
        return self._http.get(path % repo)

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
