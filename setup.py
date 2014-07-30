#!/usr/bin/env python

import os
import sys

import octokit

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably also want to tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (octokit.__version__, octokit.__version__))
    print("  git push --tags")
    sys.exit()


requires = [
    'requests>=2.0.1',
]

with open('README.md') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='octokit.py',
    packages = ['octokit'],
    version=octokit.__version__,
    description='Missing Python toolkit for the GitHub API.',
    long_description=readme + '\n\n' + history,
    author='Alexander Shchepetilnikov',
    author_email='a@irqed.io',
    url='http://github.com/irqed/octokit.py',
    download_url='https://github.com/irqed/octokit.py/tree/%s' % octokit.__version__,
    package_data={'': ['LICENSE', 'NOTICE'], },
    package_dir={'octokit': 'octokit'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
