# encoding: utf-8

"""GitHub API resources.
"""

from octokit.resources.authorizations import Authorizations
from octokit.resources.commit_comments import CommitComments
from octokit.resources.commits import Commits
from octokit.resources.contents import Contents
from octokit.resources.emojis import Emojis
from octokit.resources.events import Events
from octokit.resources.feeds import Feeds
from octokit.resources.gists import Gists
from octokit.resources.gitignore import Gitignore
from octokit.resources.hooks import Hooks
from octokit.resources.issues import Issues
from octokit.resources.labels import Labels
from octokit.resources.legacy_search import LegacySearch
from octokit.resources.markdown import Markdown
from octokit.resources.meta import Meta
from octokit.resources.milestones import Milestones
from octokit.resources.notifications import Notifications
from octokit.resources.objects import Objects
from octokit.resources.organizations import Organizations
from octokit.resources.pub_sub_hubbub import PubSubHubbub
from octokit.resources.pull_requests import PullRequests
from octokit.resources.rate_limit import RateLimit
from octokit.resources.refs import Refs
from octokit.resources.releases import Releases
from octokit.resources.repositories import Repositories
from octokit.resources.say import Say
from octokit.resources.search import Search
from octokit.resources.service_status import ServiceStatus
from octokit.resources.stats import Stats
from octokit.resources.statuses import Statuses
from octokit.resources.users import Users



__all__ = ['Authorizations', 'CommitComments', 'Commits', 'Contents', 'Emojis',
           'Events', 'Feeds', 'Gists', 'Gitignore', 'Hooks', 'Issues',
           'Labels', 'Labels', 'LegacySearch', 'Markdown', 'Meta', 'Milestones',
           'Notifications', 'Objects', 'Organizations', 'PubSubHubbub',
           'PullRequests', 'RateLimit', 'Refs', 'Releases', 'Repositories',
           'Say', 'Search', 'ServiceStatus', 'Stats', 'Statuses', 'Users']
