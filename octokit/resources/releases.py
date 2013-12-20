# encoding: utf-8

"""Methods for the Releases API
http://developer.github.com/v3/repos/releases/
"""

from octokit.resources.base import Resource


class Releases(Resource):
    """Releases API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Releases, self).__init__(**kwargs)

    def releases(self):
        """List releases for a repository

        http://developer.github.com/v3/repos/releases/#list-releases-for-a-repository
        """
        raise NotImplementedError

    def create_release(self):
        """Create a release

        http://developer.github.com/v3/repos/releases/#create-a-release
        """
        raise NotImplementedError

    def release(self):
        """Get a release

        http://developer.github.com/v3/repos/releases/#get-a-single-release
        """
        raise NotImplementedError

    def update_release(self):
        """Update a release

        http://developer.github.com/v3/repos/releases/#edit-a-release
        """
        raise NotImplementedError

    def delete_release(self):
        """Delete a release

        http://developer.github.com/v3/repos/releases/#delete-a-release
        """
        raise NotImplementedError

    def release_assets(self):
        """List release assets

        http://developer.github.com/v3/repos/releases/#list-assets-for-a-release
        """
        raise NotImplementedError

    def upload_asset(self):
        """Upload a release asset

        http://developer.github.com/v3/repos/releases/#upload-a-release-asset
        """
        raise NotImplementedError

    def release_asset(self):
        """Get a single release asset

        http://developer.github.com/v3/repos/releases/#get-a-single-release-asset
        """
        raise NotImplementedError

    def update_release_asset(self):
        """Update a release asset

        http://developer.github.com/v3/repos/releases/#edit-a-release-asset
        """
        raise NotImplementedError

    def delete_release_asset(self):
        """Delete a release asset

        http://developer.github.com/v3/repos/releases/#delete-a-release-asset
        """
        raise NotImplementedError
