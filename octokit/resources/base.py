# encoding: utf-8

"""
Base for GitHub API resources
"""

class Resource(object):
    """Base GitHub API Resource
    """
    def __init__(self, arg):
        super(Resource, self).__init__()
        self.arg = arg
