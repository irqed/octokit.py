# encoding: utf-8

"""Methods for the Repository Statistics API
http://developer.github.com/v3/repos/statistics/
"""

from octokit.resources.base import Resource


class Stats(Resource):
    """Stats API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)

    def contributors_stats(self):
        """Get contributors list with additions, deletions, and commit counts

        http://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts
        """
        raise NotImplementedError

    def commit_activity_stats(self):
        """Get the last year of commit activity data

        http://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data
        """
        raise NotImplementedError

    def code_frequency_stats(self):
        """Get the number of additions and deletions per week

        http://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week
        """
        raise NotImplementedError

    def participation_stats(self):
        """Get the weekly commit count for the repo owner and everyone else

        http://developer.github.com/v3/repos/statistics/#get-the-weekly-commit-count-for-the-repo-owner-and-everyone-else
        """
        raise NotImplementedError

    def punch_card_stats(self):
        """Get the number of commits per hour in each day

        http://developer.github.com/v3/repos/statistics/#get-the-number-of-commits-per-hour-in-each-day
        """
        raise NotImplementedError
