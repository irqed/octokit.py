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


packages = [
    'octokit',
]

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
    name='octokit',
    version=octokit.__version__,
    description='Missing Python toolkit for the GitHub API.',
    long_description=readme + '\n\n' + history,
    author='Alexander Shchepetilnikov',
    author_email='alex@irqed.com',
    url='http://github.com/irqed/octokit.py',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], },
    package_dir={'octokit': 'octokit'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
