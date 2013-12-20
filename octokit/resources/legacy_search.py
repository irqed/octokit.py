# encoding: utf-8

"""Methods for the Legacy Search API
http://developer.github.com/v3/search/
"""

from octokit.resources.base import Resource


class LegacySearch(Resource):
    """LegacySearch API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(LegacySearch, self).__init__(**kwargs)

    def legacy_search_repositories(self):
        """Legacy repository search
        http://developer.github.com/v3/search/#search-repositories
        """
        raise NotImplementedError

    def legacy_search_issues(self):
        """Legacy search issues within a repository
        """
        raise NotImplementedError

    def legacy_search_users(self):
        """Search for user
        http://developer.github.com/v3/search/#search-users
        """
        raise NotImplementedError
