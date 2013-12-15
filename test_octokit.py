#!/usr/bin/env python
# encoding: utf-8

"""Tests for Octokit.
"""

import os
import pytest
import unittest

import octokit


class AuthenticationTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_not_authenticated(self):
        hub = octokit.Octokit(trust_env=False)
        self.assertEqual(hub.authenticated, False)

    def test_authenticated_by_env(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.authenticated, True)

    def test_basic_authenticated(self):
        login = os.environ.get('OCTOKIT_LOGIN')
        password = os.environ.get('OCTOKIT_PASSWORD')

        hub = octokit.Octokit(login=login, password=password)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.basic_authenticated, True)

    def test_token_authenticated(self):
        token = os.environ.get('OCTOKIT_ACCESS_TOKEN')
        hub = octokit.Octokit(access_token=token)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.token_authenticated, True)

    def test_application_authenticated(self):
        client_id = os.environ.get('OCTOKIT_CLIENT_ID')
        client_secret = os.environ.get('OCTOKIT_SECRET')
        hub = octokit.Octokit(client_id=client_id, client_secret=client_secret)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.application_authenticated, True)

    def test_user_authenticated(self):
        login = os.environ.get('OCTOKIT_LOGIN')
        password = os.environ.get('OCTOKIT_PASSWORD')
        hub = octokit.Octokit(login=login, password=password)

        token = os.environ.get('OCTOKIT_ACCESS_TOKEN')
        hub_two = octokit.Octokit(access_token=token)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub_two.authenticated, True)

        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub_two.user_authenticated, True)


class UserTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_current_user(self):
        hub = octokit.Octokit()
        current_user = hub.user.get()
        self.assertEqual(current_user['login'], 'octopy')


class UsersTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_get_users(self):
        hub = octokit.Octokit()
        users = hub.users.get()
        self.assertEqual(len(users), 100)
