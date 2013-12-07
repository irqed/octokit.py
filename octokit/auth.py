# encoding: utf-8

"""
Github auth backends for requests.
"""


from requests.auth import AuthBase, HTTPBasicAuth


class HTTPTokenAuth(AuthBase):
    """Auth class to use with GitHub's access_token
    """
    def __init__(self):
        super(HTTPTokenAuth, self).__init__()
