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
        http://developer.github.com/v3/activity/notifications/#list-your-notifications
        """
        return self._http.get('notifications')

    def repository_notifications(self):
        """List your notifications in a repository
        http://developer.github.com/v3/activity/notifications/#list-your-notifications-in-a-repository
        """
        raise NotImplementedError

    def mark_notifications_as_read(self):
        """Mark notifications as read
        http://developer.github.com/v3/activity/notifications/#mark-as-read
        """
        raise NotImplementedError

    def mark_repository_notifications_as_read(self):
        """Mark notifications from a specific repository as read
        http://developer.github.com/v3/activity/notifications/#mark-notifications-as-read-in-a-repository
        """
        raise NotImplementedError

    def thread_notifications(self):
        """List notifications for a specific thread
        http://developer.github.com/v3/activity/notifications/#view-a-single-thread
        """
        raise NotImplementedError

    def mark_thread_as_read(self):
        """Mark thread as read
        http://developer.github.com/v3/activity/notifications/#mark-a-thread-as-read
        """
        raise NotImplementedError

    def thread_subscription(self):
        """Get thread subscription
        http://developer.github.com/v3/activity/notifications/#get-a-thread-subscription
        """
        raise NotImplementedError

    def update_thread_subscription(self):
        """Update thread subscription
        http://developer.github.com/v3/activity/notifications/#set-a-thread-subscription
        """
        raise NotImplementedError

    def delete_thread_subscription(self):
        """Delete a thread subscription
        http://developer.github.com/v3/activity/notifications/#delete-a-thread-subscription
        """
        raise NotImplementedError
