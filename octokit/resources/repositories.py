# encoding: utf-8

"""Methods for the Repositories API
http://developer.github.com/v3/repos/
"""

from octokit.resources.base import Resource


class Repositories(Resource):
    """Repositories API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Repositories, self).__init__(**kwargs)

    def repository_exists(self):
        """Check if a repository exists

        http://developer.github.com/v3/repos/#get
        """
        raise NotImplementedError

    def repository(self):
        """Get a single repository

        http://developer.github.com/v3/repos/#get
        """
        raise NotImplementedError

    def edit_repository(self):
        """Edit a repository

        http://developer.github.com/v3/repos/#edit
        """
        raise NotImplementedError

    def repositories(self):
        """List repositories

        http://developer.github.com/v3/repos/#list-your-repositories
        """
        raise NotImplementedError

    def all_repositories(self):
        """List all repositories

        This provides a dump of every repository, in the order that they were
        created.

        http://developer.github.com/v3/repos/#list-all-public-repositories
        """
        raise NotImplementedError

    def star(self):
        """Star a repository

        http://developer.github.com/v3/activity/starring/#star-a-repository
        """
        raise NotImplementedError

    def unstar(self):
        """Unstar a repository

        http://developer.github.com/v3/activity/starring/#unstar-a-repository
        """
        raise NotImplementedError

    def watch(self):
        """Watch a repository

        http://developer.github.com/v3/activity/watching/#watch-a-repository-legacy
        """
        raise NotImplementedError

    def unwatch(self):
        """Unwatch a repository

        http://developer.github.com/v3/activity/watching/#stop-watching-a-repository-legacy
        """
        raise NotImplementedError

    def fork(self):
        """Fork a repository

        http://developer.github.com/v3/repos/forks/#create-a-fork
        """
        raise NotImplementedError

    def create_repository(self):
        """Create a repository for a user or organization

        http://developer.github.com/v3/repos/#create
        """
        raise NotImplementedError

    def delete_repository(self):
        """Delete repository

        Note: If OAuth is used, 'delete_repo' scope is required

        http://developer.github.com/v3/repos/#delete-a-repository
        """
        raise NotImplementedError

    def set_private(self):
        """Hide a public repository
        """
        raise NotImplementedError

    def set_public(self):
        """Unhide a private repository
        """
        raise NotImplementedError

    def deploy_keys(self):
        """Get deploy keys on a repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/keys/#list
        """
        raise NotImplementedError

    def deploy_key(self):
        """Get a single deploy key for a repo

        http://developer.github.com/v3/repos/keys/#get
        """
        raise NotImplementedError

    def add_deploy_key(self):
        """Add deploy key to a repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/keys/#create
        """
        raise NotImplementedError

    def edit_deploy_key(self):
        """Edit a deploy key

        Requires authenticated client.

        http://developer.github.com/v3/repos/keys/#edit
        """
        raise NotImplementedError

    def remove_deploy_key(self):
        """Remove deploy key from a repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/keys/#delete
        """
        raise NotImplementedError

    def collaborators(self):
        """List collaborators

        http://developer.github.com/v3/repos/collaborators/#list
        """
        raise NotImplementedError

    def add_collaborator(self):
        """Add collaborator to repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/collaborators/#add-collaborator
        """
        raise NotImplementedError

    def remove_collaborator(self):
        """Remove collaborator from repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/collaborators/#remove-collaborator
        """
        raise NotImplementedError

    def is_collaborator(self):
        """Checks if a user is a collaborator for a repo

        Requires authenticated client.

        http://developer.github.com/v3/repos/collaborators/#get
        """
        raise NotImplementedError

    def repository_teams(self):
        """List teams for a repo

        Requires authenticated client that is an owner or collaborator of the repo.

        http://developer.github.com/v3/repos/#list-teams
        """
        raise NotImplementedError

    def contributors(self):
        """List contributors to a repo

        Requires authenticated client for private repos.

        http://developer.github.com/v3/repos/#list-contributors
        """
        raise NotImplementedError

    def stargazers(self):
        """List stargazers of a repo

        Requires authenticated client for private repos.

        http://developer.github.com/v3/activity/starring/#list-stargazers
        """
        raise NotImplementedError

    def forks(self):
        """List forks

        Requires authenticated client for private repos.

        http://developer.github.com/v3/repos/forks/#list-forks
        """
        raise NotImplementedError

    def languages(self):
        """List languages of code in the repo

        Requires authenticated client for private repos.

        http://developer.github.com/v3/repos/#list-languages
        """
        raise NotImplementedError

    def tags(self):
        """List tags

        Requires authenticated client for private repos.

        http://developer.github.com/v3/repos/#list-tags
        """
        raise NotImplementedError

    def branches(self):
        """List branches

        Requires authenticated client for private repos.

        http://developer.github.com/v3/repos/#list-branches
        """
        raise NotImplementedError

    def branch(self):
        """Get a single branch from a repository

        http://developer.github.com/v3/repos/#get-branch
        """
        raise NotImplementedError

    def hooks(self):
        """List repo hooks

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#list
        """
        raise NotImplementedError

    def hook(self):
        """Get single hook

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#get-single-hook
        """
        raise NotImplementedError

    def create_hook(self):
        """Create a hook

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#create-a-hook
        """
        raise NotImplementedError

    def edit_hook(self):
        """Edit a hook

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#edit-a-hook
        """
        raise NotImplementedError

    def remove_hook(self):
        """Delete hook

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#delete-a-hook
        """
        raise NotImplementedError

    def test_hook(self):
        """Test hook

        Requires authenticated client.

        http://developer.github.com/v3/repos/hooks/#test-a-push-hook
        """
        raise NotImplementedError

    def repository_assignees(self):
        """List users available for assigning to issues

        Requires authenticated client for private repos.

        http://developer.github.com/v3/issues/assignees/#list-assignees
        """
        raise NotImplementedError

    def check_assignee(self):
        """Check to see if a particular user is an assignee for a repository

        http://developer.github.com/v3/issues/assignees/#check-assignee
        """
        raise NotImplementedError

    def subscribers(self):
        """List watchers subscribing to notifications for a repo

        http://developer.github.com/v3/activity/watching/#list-watchers
        """
        raise NotImplementedError

    def subscription(self):
        """Get a repository subscription

        http://developer.github.com/v3/activity/watching/#get-a-repository-subscription
        """
        raise NotImplementedError

    def update_subscription(self):
        """Update repository subscription

        http://developer.github.com/v3/activity/watching/#set-a-repository-subscription
        """
        raise NotImplementedError

    def delete_subscription(self):
        """Delete a repository subscription

        http://developer.github.com/v3/activity/watching/#delete-a-repository-subscription
        """
        raise NotImplementedError
