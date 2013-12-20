# encoding: utf-8

"""Methods for the Organizations API
http://developer.github.com/v3/orgs/
"""

from octokit.resources.base import Resource


class Organizations(Resource):
    """Organizations API resource
    """
    url = None

    def __init__(self, **kwargs):
        super(Organizations, self).__init__(**kwargs)

    def organization(self):
        """Get an organization

        http://developer.github.com/v3/orgs/#get-an-organization
        """
        raise NotImplementedError

    def update_organization(self):
        """Update an organization

        Requires authenticated client with proper organization permissions.

        http://developer.github.com/v3/orgs/#edit-an-organization
        """
        raise NotImplementedError

    def organizations(self):
        """Get organizations for a user

        Nonauthenticated calls to this method will return organizations that
        the user is a public member. Use an authenicated client to get both
        public and private organizations for a user.

        http://developer.github.com/v3/orgs/#list-user-organizations
        """
        raise NotImplementedError

    def organization_repositories(self):
        """List organization repositories

        Public repositories are available without authentication. Private repos
        require authenticated organization member.

        http://developer.github.com/v3/repos/#list-organization-repositories
        """
        raise NotImplementedError

    def organization_members(self):
        """Get organization members

        Public members of the organization are returned by default. An
        authenticated client that is a member of the GitHub organization
        is required to get private members.

        http://developer.github.com/v3/orgs/members/#members-list
        """
        raise NotImplementedError

    def organization_public_members(self):
        """Get organization public members

        Lists the public members of an organization

        http://developer.github.com/v3/orgs/members/#public-members-list
        """
        raise NotImplementedError

    def is_organization_member(self):
        """Check if a user is a member of an organization

        Use this to check if another user is a member of an organization that
        you are a member. If you are not in the organization you are checking,
        use .is_organization_public_member instead.

        http://developer.github.com/v3/orgs/members/#check-membership
        """
        raise NotImplementedError

    def is_organization_public_member(self):
        """Check if a user is a public member of an organization

        If you are checking for membership of a user of an organization that
        you are in, use .is_organization_member instead.

        http://developer.github.com/v3/orgs/members/#check-public-membership
        """
        raise NotImplementedError

    def organization_teams(self):
        """List teams

        Requires authenticated organization member.

        http://developer.github.com/v3/orgs/teams/#list-teams
        """
        raise NotImplementedError

    def create_team(self):
        """Create team

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/teams/#create-team
        """
        raise NotImplementedError

    def team(self):
        """Get team

        Requires authenticated organization member.

        http://developer.github.com/v3/orgs/teams/#get-team
        """
        raise NotImplementedError

    def update_team(self):
        """Update team

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/teams/#edit-team
        """
        raise NotImplementedError

    def delete_team(self):
        """Delete team

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/teams/#delete-team
        """
        raise NotImplementedError

    def team_members(self):
        """List team members

        Requires authenticated organization member.

        http://developer.github.com/v3/orgs/teams/#list-team-members
        """
        raise NotImplementedError

    def add_team_member(self):
        """Add team member

        Requires authenticated organization owner or member with team
        `admin` permission.

        http://developer.github.com/v3/orgs/teams/#add-team-member
        """
        raise NotImplementedError

    def remove_team_member(self):
        """Remove team member

        Requires authenticated organization owner or member with team
        `admin` permission.

        http://developer.github.com/v3/orgs/teams/#remove-team-member
        """
        raise NotImplementedError

    def is_team_member(self):
        """Check if a user is a member of a team

        Use this to check if another user is a member of a team that
        you are a member.

        http://developer.github.com/v3/orgs/teams/#get-team-member
        """
        raise NotImplementedError

    def team_repositories(self):
        """List team repositories

        Requires authenticated organization member.

        http://developer.github.com/v3/orgs/teams/#list-team-repos
        """
        raise NotImplementedError

    def is_team_repository(self):
        """Check if a repo is managed by a specific team

        http://developer.github.com/v3/orgs/teams/#get-team-repo
        """
        raise NotImplementedError

    def add_team_repository(self):
        """Add team repository

        Requires authenticated user to be an owner of the organization that the
        team is associated with. Also, the repo must be owned by the
        organization, or a direct form of a repo owned by the organization.

        http://developer.github.com/v3/orgs/teams/#add-team-repo
        """
        raise NotImplementedError

    def remove_team_repository(self):
        """Remove team repository

        Removes repository from team. Does not delete the repository.

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/teams/#remove-team-repo
        """
        raise NotImplementedError

    def remove_organization_member(self):
        """Remove organization member

        Requires authenticated organization owner or member with team
        `admin` access.

        http://developer.github.com/v3/orgs/members/#remove-a-member
        """
        raise NotImplementedError

    def publicize_membership(self):
        """Publicize a user's membership of an organization

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/members/#publicize-a-users-membership
        """
        raise NotImplementedError

    def unpublicize_membership(self):
        """Conceal a user's membership of an organization.

        Requires authenticated organization owner.

        http://developer.github.com/v3/orgs/members/#conceal-a-users-membership
        """
        raise NotImplementedError

    def user_teams(self):
        """List all teams for the authenticated user across all their orgs

        http://developer.github.com/v3/orgs/teams/#list-user-teams
        """
        raise NotImplementedError
