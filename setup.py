#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('octokit/version.py').read())

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably also want to tag the version now:")
    print("\tgit tag -a %s -m 'version %s'" % (__version__, __version__))
    print("\tgit push --tags")
    sys.exit()


requires = [
    'slumber==0.6.0',
]


with open('README.md') as f:
    readme = f.read()

with open('HISTORY.rst') as f:
    history = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='octokit.py',
    version=__version__,
    description='Python toolkit for GitHub API',
    long_description=readme + '\n\n' + history,

    license=license,

    author='Alexander Shchepetilnikov',
    author_email='a@irqed.io',

    packages=['octokit'],
    package_dir={'octokit': 'octokit'},
    package_data={'': ['LICENSE', 'NOTICE'], },

    zip_safe=False,
    include_package_data=True,
    install_requires=requires,

    url='http://github.com/irqed/octokit.py',
    download_url=('https://github.com/irqed/octokit.py/tree/%s' % __version__),

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
