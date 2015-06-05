Octokit.py: GitHub API toolkit
=========================
It's a small library written in Python to query GitHub API in a quick and easy way.

[![PyPi Downloads](https://img.shields.io/pypi/dm/octokit.py.svg)](https://pypi.python.org/pypi/octokit.py/0.1.1)
[![PyPi Version](https://img.shields.io/pypi/v/octokit.py.svg)](https://pypi.python.org/pypi/octokit.py/0.1.1)
[![Build Status](https://img.shields.io/travis/irqed/octokit.py.svg)](https://travis-ci.org/irqed/octokit.py)
[![Coverage Status](https://img.shields.io/coveralls/irqed/octokit.py.svg)](https://coveralls.io/r/irqed/octokit.py?branch=master)

Features
--------
* Clean and easy interface
* Completely reflects GitHub API V3 (except gists)
* Dot notation
* 100% test coverage 


Requirements
--------
* Python 2.6/2.7 (Python 3 support is blocked by slumber, but should be fixed soon)
* slumber

Installation
------------
```
  pip install octokit.py
```

Examples
-------------
To get a list of user's repositories:
```python
>>> hub = Octokit()
>>> print hub.users('irqed').repos.get()
```
or
```python
>>> print hub.users.irqed.repos.get()
```

To use basic authorization just pass your login and password
```python
>>> hub = Octokit(login='username', password='secret_password')
>>> print hub.repos.irqed('octokit.py').issues.get()
```

To use access token:
```python
>>> hub = Octokit(access_token='so_secret_wow')
```

Documentation
-------------

Alternatives
-------------
* [PyGithub](https://github.com/jacquev6/PyGithub)
* [Pygithub3](https://github.com/copitux/python-github3)
* [libsaas](https://github.com/ducksboard/libsaas)
* [github3.py](https://github.com/sigmavirus24/github3.py)
* [sanction](https://github.com/demianbrecht/sanction)
* [agithub](https://github.com/jpaugh/agithub)
* [githubpy](https://github.com/michaelliao/githubpy)
* [octohub](https://github.com/turnkeylinux/octohub)
* [Github-Flask](http://github-flask.readthedocs.org/)
* [torngithub](https://github.com/jkeylu/torngithub)
