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

    def test_info(self):
        hub = octokit.Octokit()
        user = hub.user.info()
        self.assertEqual(user['login'], 'octopy')

    def test_update(self):
        hub = octokit.Octokit()
        payload = dict(name='octo py', email='octo@irqed.com', blog='octo blog',
                       company='octo inc', location='moscow', hireable=False,
                       bio='meh')
        user = hub.user.update(payload)
        self.assertEqual(user['location'], 'moscow')

    def test_followers(self):
        hub = octokit.Octokit()
        followers = hub.user.followers()
        self.assertEqual(type(followers), list)

class UsersTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True
"""
    def test_all_users(self):
        hub = octokit.Octokit()
        users = hub.users.all_users()
        self.assertEqual(len(users), 100)

    def test_user(self):
        hub = octokit.Octokit()
        user = hub.users.user('irqed')
        self.assertEqual(user['login'], 'irqed')

    def test_user_404(self):
        hub = octokit.Octokit()
        with self.assertRaises(octokit.errors.OctokitNotFoundError):
            user = hub.users.user('irqed_blah_irqed')

    def test_followers(self):
        hub = octokit.Octokit()
        followers = hub.users.followers('irqed')
        self.assertEqual(type(followers), list)

    def test_following(self):
        hub = octokit.Octokit()
        following = hub.users.following('irqed')
        self.assertEqual(type(following), list)
        self.assertNotEqual(len(following), 0)

    def test_current_user_following(self):
        hub = octokit.Octokit()
        following = hub.users.following()
        self.assertEqual(type(following), list)

    def test_user_follows(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.users.follows('octopy', 'irqed'), False)

    def test_user_follows_true(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.users.follows('sashka', 'irqed'), True)

    def test_current_user_follows(self):
        hub = octokit.Octokit()
        hub.users.follow('irqed')
        self.assertEqual(hub.users.follows('irqed'), True)
        hub.users.unfollow('irqed')

    def test_starred(self):
        hub = octokit.Octokit()
        starred = hub.users.starred()
        self.assertEqual(type(starred), list)
        self.assertEqual(len(starred), 0)

    def test_user_starred(self):
        hub = octokit.Octokit()
        starred = hub.users.starred('irqed')
        self.assertEqual(type(starred), list)
        self.assertNotEqual(len(starred), 0)

    def test_is_starred(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.users.is_starred('irqed/tornado'), False)

    def test_user_keys(self):
        hub = octokit.Octokit()
        starred = hub.users.keys('irqed')
        self.assertEqual(type(starred), list)

    def test_current_user_keys(self):
        hub = octokit.Octokit()
        keys = hub.users.keys()
        self.assertEqual(type(keys), list)
        self.assertEqual(len(keys), 1)

    def test_add_remove_key(self):
        hub = octokit.Octokit()
        key = hub.users.add_key(title="test_key", key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAB+wC/1cFsriBGEM2/krbfVRWMeL0xIs9W/B8H0vTTCiR3rI7QpBGGMlZeYPB8K5HlUZAq2ryRPphX0hMkGwCAAkhfVlohuZkMNOpeFANKdw3q2jdQjSH57KCpdj2wNjFZAgJvgsYPmTTH+DLVMpVUqtskJOsTYmU/O51//9X2EuUahSuS8pq48CmRgSo9PSKEqY63RLsFhwPYh+FW21L65i8mYep0/hhyI0kVuZmjwSN2HMk5X4dFXdCe2wX3kRo3d7EQ4d0ONnZNQtMgYGlYHknLfwLWWU+UFPeqjA8Su58KEdIji5nko2OW+afe+aaicsm9MloiopPR+XR39sGSlDibdaHtCcoVDXHNqDbnGfhyq/2+dAzo/b8vQ4ZyzudX86OqatjKMt2F0fJwcqwQll08sGCuYq+sb8RDjW0ybgTHmhAFgJ3pzwAVjhMdMz3OiqfhFCqk8KDZ9tn4xwBAXOM5W94HLmSZGxvhylopqGDhjnuk1d59L8JVcv4s5Aau+DhRl1h265YYxq6vsdrw7F7be3IqbSQEi6sPyg+tbpM9CJaOS7wokWCdzk6oeket/83QMdBa+QpEjmtr86oG+Ixa2KWQ9ecDM4sCQz24A+7InFDKnJjRoqScpdU5Cubf3QV3No+zO/HRgct4wUxWvkY1YkJDEUzk+JGLqQ== octopy_test_key")
        self.assertEqual(type(key), dict)
        self.assertEqual(hub.users.remove_key(key['id']), True)

    def test_update_key(self):
        hub = octokit.Octokit()
        key = hub.users.update_key(6620193, title="!test_key!")
        self.assertEqual(key['title'], "!test_key!")

    def test_emails(self):
        hub = octokit.Octokit()
        emails = hub.users.emails()
        self.assertEqual(type(emails), list)
        self.assertNotEqual(len(emails), 0)

    def test_add_remove_email(self):
        hub = octokit.Octokit()
        email = hub.users.add_email(email=['octo_test@irqed.com'])
        self.assertEqual(type(emails), dict)
        self.assertEqual(hub.users.remove_email(email=['octo_test@irqed.com']),
                         True)
"""
"""
class Authorizations(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_list_authorizations(self):
        hub = octokit.Octokit()
        authorizations = hub.authorizations.get()
        self.assertEqual(len(authorizations), 1)

    def test_get_single_authorization(self):
        hub = octokit.Octokit()
        authorization = hub.authorizations.get(id=4760713)
        self.assertIn('token', authorization)

    def test_get_single_authorization_404(self):
        hub = octokit.Octokit()
        with self.assertRaises(octokit.OctokitError):
            authorization = hub.authorizations.get(id=666)


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
"""
