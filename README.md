Octokit.py: GitHub API toolkit
=========================
It's a small library written in Python to query GitHub API in a quick and easy way.

[![Build Status](https://travis-ci.org/irqed/octokit.py.svg?branch=master)](https://travis-ci.org/irqed/octokit.py)
[![Coverage Status](https://coveralls.io/repos/irqed/octokit.py/badge.png?branch=master)](https://coveralls.io/r/irqed/octokit.py?branch=master)
[![PyPi version](https://pypip.in/v/octokit.py/badge.png)](https://crate.io/packages/octokit.py/)
[![PyPi downloads](https://pypip.in/d/octokit.py/badge.png)](https://crate.io/packages/octokit.py/)

Features
--------

Requirements
--------
* Python 2.6/2.7 (Python 3 support is blocked by slumber, but should be fixed soon)
* slumber

Installation
------------
Note: PyPi package isn't updated yet.
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
