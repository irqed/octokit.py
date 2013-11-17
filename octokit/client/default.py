# encoding: utf-8

from .. import __version__


class Default(object):
    """Default configuration options for Client"""

    # Default API endpoint
    API_ENDPOINT = "https://api.github.com"

    # Default User Agent header string
    USER_AGENT   = "Octokit.py/%s" % __version__

    # Default media type
    MEDIA_TYPE   = "application/vnd.github.beta+json"

    # Default WEB endpoint
    WEB_ENDPOINT = "https://github.com"
