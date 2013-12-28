# encoding: utf-8

"""Methods for the Notifications API
http://developer.github.com/v3/activity/notifications/
"""

from octokit.resources.base import Resource


class Notifications(Resource):
    """Notifications API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Notifications, self).__init__(**kwargs)

    def all(self):
        """List your notifications

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#list-your-notifications
        """
        return self._http.get('notifications')

    def repository(self, repo):
        """List your notifications in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#list-your-notifications-in-a-repository
        """
        return self._http.get('repos/%s/notifications' % repo)

    def mark_as_read(self, unread=False, last_read_at=None):
        """Mark notifications as read

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#mark-as-read
        """
        payload = dict(read=True, unread=False)
        if unread:
            payload['read'] = False
            payload['unread'] = True

        if last_read_at:
            payload['last_read_at'] = last_read_at

        url = self._http._settings.api_endpoint + 'notifications'

        r = self._http._request('PUT', url, payload=payload)
        return True if r.status_code == 205 else False

    def mark_repository_as_read(self):
        """Mark notifications from a specific repository as read

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#mark-notifications-as-read-in-a-repository
        """
        raise NotImplementedError

    def thread(self):
        """List notifications for a specific thread

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#view-a-single-thread
        """
        raise NotImplementedError

    def mark_thread_as_read(self):
        """Mark thread as read

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#mark-a-thread-as-read
        """
        raise NotImplementedError

    def thread_subscription(self):
        """Get thread subscription

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#get-a-thread-subscription
        """
        raise NotImplementedError

    def update_thread_subscription(self):
        """Update thread subscription

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#set-a-thread-subscription
        """
        raise NotImplementedError

    def remove_thread_subscription(self):
        """Delete a thread subscription

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#delete-a-thread-subscription
        """
        raise NotImplementedError
