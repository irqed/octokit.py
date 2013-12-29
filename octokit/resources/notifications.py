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

    def _mark_methods_payload(self, unread=False, last_read_at=None):
        """Returns a payload for mark_* Methods
        """
        payload = dict(read=True, unread=False)
        if unread:
            payload['read'] = False
            payload['unread'] = True

        if last_read_at:
            payload['last_read_at'] = last_read_at

        return payload

    def _get_params(self, **kwargs):
        params = dict()
        for key, value in kwargs.items():
            if value:
                params[key] = 'true' if type(value) is bool else value
        return params

    def all(self, all=False, participating=False, since=None):
        """List your notifications

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#list-your-notifications
        """
        params = self._get_params(all=all, participating=participating,
                                  since=since)
        return self._http.get('notifications', params=params)

    def repository(self, repo, all=False, participating=False, since=None):
        """List your notifications in a repository

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#list-your-notifications-in-a-repository
        """
        params = self._get_params(all=all, participating=participating,
                                  since=since)
        return self._http.get('repos/%s/notifications' % repo, params=params)

    def mark_as_read(self, unread=False, last_read_at=None):
        """Mark notifications as read

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#mark-as-read
        """
        payload = self._mark_methods_payload(unread, last_read_at)
        url = self._http._settings.api_endpoint + 'notifications'
        r = self._http._request('PUT', url, payload=payload)
        return True if r.status_code == 205 else False

    def mark_repository_as_read(self, repo, unread=False, last_read_at=None):
        """Mark notifications from a specific repository as read

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#mark-notifications-as-read-in-a-repository
        """
        payload = self._mark_methods_payload(unread, last_read_at)
        url = self._http._settings.api_endpoint + 'repos/%s/notifications' % repo
        r = self._http._request('PUT', url, payload=payload)
        return True if r.status_code == 205 else False

    def thread(self, thread_id):
        """List notifications for a specific thread

        Requries an authenticated client.

        http://developer.github.com/v3/activity/notifications/#view-a-single-thread
        """
        return self._http.get('notifications/threads/%s' % thread_id)

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
