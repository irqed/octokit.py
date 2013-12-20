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

    def test_update_user(self):
        hub = octokit.Octokit()
        current_user = hub.user.update(name='octo py', email='octo@irqed.com',
                                       blog='octo blog', company='octo inc',
                                       location='moscow', hireable=True,
                                       bio='meh')

        self.assertEqual(current_user['location'], 'moscow')


class UsersTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_list_users(self):
        hub = octokit.Octokit()
        users = hub.users.get()
        self.assertEqual(len(users), 100)

    def test_get_user_by_login(self):
        hub = octokit.Octokit()
        user = hub.users.get(login='irqed')
        self.assertEqual(user['login'], 'irqed')

    def test_get_user_by_404(self):
        hub = octokit.Octokit()
        with self.assertRaises(octokit.OctokitError):
            user = hub.users.get(login='irqed_blah_irqed')


class Authorizations(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_list_authorizations(self):
        hub = octokit.Octokit()
        authorizations = hub.authorizations.get()
        self.assertEqual(len(authorizations), 1)


class EmojisTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_list_emojis(self):
        hub = octokit.Octokit()
        emojis = hub.emojis.get()
        self.assertIn('+1', emojis)


class GitignoreTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_list_gitignore_templates(self):
        hub = octokit.Octokit()
        templates = hub.gitignore.get()
        self.assertIn('Python', templates)

    def test_get_gitignore_template_by_lang(self):
        hub = octokit.Octokit()
        template = hub.gitignore.get(lang='Python')
        self.assertIn('source', template)


class MetaTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_get_github_meta(self):
        hub = octokit.Octokit()
        meta = hub.meta.get()
        self.assertIn('hooks', meta)


class ServiceStatusTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_get_status_links(self):
        hub = octokit.Octokit()
        service = hub.service_status.get()
        self.assertIn('status_url', service)

    def test_status(self):
        hub = octokit.Octokit()
        self.assertIn('status', hub.service_status.status)

    def test_status(self):
        hub = octokit.Octokit()
        self.assertIn('body', hub.service_status.last_message)

    def test_messages(self):
        hub = octokit.Octokit()
        self.assertNotEqual(len(hub.service_status.messages), 0)
