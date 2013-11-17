# encoding: utf-8

"""
Default options for a Client.
"""

from os import environ as env
from collections import namedtuple

from octokit import __version__


# Default API endpoint
API_ENDPOINT = "https://api.github.com"

# Default User Agent header string
USER_AGENT   = "Octokit.py/%s" % __version__

# Default media type
MEDIA_TYPE   = "application/vnd.github.beta+json"

# Default WEB endpoint
WEB_ENDPOINT = "https://github.com"

_O = namedtuple('Options',
                'api_endpoint, user_agent, media_type, web_endpoint,\
                 access_token, auto_paginate, client_id, client_secret,\
                 login, password, page_size, proxy')

DEFAULTS = _O(
    api_endpoint=env.get('OCTOKIT_API_ENDPOINT') or API_ENDPOINT,
    web_endpoint=env.get('OCTOKIT_WEB_ENDPOINT') or WEB_ENDPOINT,

    user_agent=env.get('OCTOKIT_USER_AGENT') or USER_AGENT,
    media_type=env.get('OCTOKIT_MEDIA_TYPE') or MEDIA_TYPE,

    access_token=env.get('OCTOKIT_ACCESS_TOKEN', None),
    auto_paginate=env.get('OCTOKIT_AUTO_PAGINATE', None),
    client_id=env.get('OCTOKIT_CLIENT_ID', None),
    client_secret=env.get('OCTOKIT_SECRET', None),
    login=env.get('OCTOKIT_LOGIN', None),
    password=env.get('OCTOKIT_PASSWORD', None),
    page_size=int(env.get('OCTOKIT_PER_PAGE', 10)),
    proxy=env.get('OCTOKIT_PROXY', None)
)
