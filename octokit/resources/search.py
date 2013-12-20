# encoding: utf-8

"""Methods for the Search API
http://developer.github.com/v3/search/
"""

from octokit.resources.base import Resource


class Search(Resource):
    """Search API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

    def search_code(self):
        """Search code

        http://developer.github.com/v3/search/#search-code
        """
        raise NotImplementedError

    def search_issues(self):
        """Search issues

        http://developer.github.com/v3/search/#search-issues
        """
        raise NotImplementedError

    def search_repositories(self):
        """Search repositories

        http://developer.github.com/v3/search/#search-repositories
        """
        raise NotImplementedError

    def search_users(self):
        """Search users

        http://developer.github.com/v3/search/#search-users
        """
        raise NotImplementedError
