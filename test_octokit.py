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


class Authorizations(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_all(self):
        hub = octokit.Octokit()
        authorizations = hub.authorizations.all()
        self.assertEqual(type(authorizations), list)

    def test_authorization(self):
        hub = octokit.Octokit()
        authorization = hub.authorizations.authorization(4760713)
        self.assertIn('token', authorization)

    def test_authorization_404(self):
        hub = octokit.Octokit()
        with self.assertRaises(octokit.errors.OctokitNotFoundError):
            hub.authorizations.authorization(666)


class EmojisTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_all(self):
        hub = octokit.Octokit()
        emojis = hub.emojis.all()
        self.assertIn('+1', emojis)


class GitignoreTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_templates(self):
        hub = octokit.Octokit()
        templates = hub.gitignore.templates()
        self.assertEqual(type(templates), list)
        self.assertNotEqual(len(templates), 0)

    def test_template(self):
        hub = octokit.Octokit()
        template = hub.gitignore.template('Python')
        self.assertEqual(type(template), dict)


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

    def test_following(self):
        hub = octokit.Octokit()
        following = hub.user.following()
        self.assertEqual(type(following), list)

    def test_follows(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.user.follows('spoof'), False)

    def test_follow_unfollow(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.user.follow('irqed'), True)
        self.assertEqual(hub.user.follows('irqed'), True)
        self.assertEqual(hub.user.unfollow('irqed'), True)

    def test_starred(self):
        hub = octokit.Octokit()
        starred = hub.user.starred()
        self.assertEqual(type(starred), list)
        self.assertEqual(len(starred), 0)

    def test_is_starred(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.user.is_starred('irqed/tornado'), False)

    def test_key(self):
        hub = octokit.Octokit()
        key = hub.user.key(6620193)
        self.assertEqual(type(key), dict)

    def test_keys(self):
        hub = octokit.Octokit()
        keys = hub.user.keys()
        self.assertEqual(type(keys), list)

    def test_update_key(self):
        hub = octokit.Octokit()
        payload = dict(title="!test_key!")
        key = hub.user.update_key(6620193, payload)
        self.assertEqual(key['title'], "!test_key!")

    def test_add_remove_key(self):
        hub = octokit.Octokit()
        payload = dict(title="test_key2", key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAB+wDCfyqs4CBjM5jav9GSInhO8xHPq6u2ftRs1IJDuPQI0RgeAwyIWT6Ve2FXMSkPC3USUv8yA/rE8/x/T2/6oq/QYAdyPiUpzyQwIe8JlacPrk9hjvjtcEIE5AdoRjrvXT9D+FDV1MobIEcexNmgRkdAcJOSV9sOfUjwH43F7p8exZ19SbQ4hoAhUlD0wXxufG+QDk0Mdov0tSMTtJaJcAn+NX+1EGylTtkLOCAQv2x3Lov6tkcyNAwC+MZMHLxgwz4d3vvnlQFlN6DdCwHzffrYk8lTgZ36RVCfg5Ik3kB8BgePllay87JsKfo7g48JIOm9Ho17LNpvXt/ce8LTELPG58pj2vQMFzfh2L8V6eq/4B3hu9CHc+45Z2KYX5q0hQ26KuIJdeAAygsLPFCVQL6kwM0lvQDJH0S8lSAFKxtqG/NVrlSZEOrh/VWOWZXZwNtl4khHP0gtwpiEhzw2bqulUR5b9A+GKRP35XrLlRR0PpeoG6vFrzglN05n/61J1zVGWFbU/dewIiyaYCPLgFlRYXzrX08oeYNVMfqtU5lk81s0G8o3/h033oxKtofhlQdY2mzhtJxUHHuGtqFBCsGFCZ8vc9PXZ+UodZvHxyAHlCcku4ItnCX3QiI7/cMB8bM1/C//baJ0lHCdFvNhxDm0Cs2g94F93ThFxw== octopy_test_key")
        key = hub.user.add_key(payload)
        self.assertEqual(type(key), dict)
        self.assertEqual(hub.user.remove_key(key['id']), True)

    def test_emails(self):
        hub = octokit.Octokit()
        emails = hub.user.emails()
        self.assertEqual(type(emails), list)
        self.assertNotEqual(len(emails), 0)

    def test_add_remove_email(self):
        hub = octokit.Octokit()
        emails = hub.user.add_email(['octo_test@irqed.com', ])
        self.assertEqual(type(emails), list)
        self.assertEqual(hub.user.remove_email(['octo_test@irqed.com', ]), True)

    def test_subscriptions(self):
        hub = octokit.Octokit()
        subscriptions = hub.user.subscriptions()
        self.assertEqual(type(subscriptions), list)


class UsersTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_all(self):
        hub = octokit.Octokit()
        users = hub.users.all()
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

    def test_follows(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.users.follows('irqed', 'octopy'), False)
        self.assertEqual(hub.users.follows('irqed', 'spoof'), True)

    def test_starred(self):
        hub = octokit.Octokit()
        starred = hub.users.starred('irqed')
        self.assertEqual(type(starred), list)

    def test_keys(self):
        hub = octokit.Octokit()
        keys = hub.users.keys('irqed')
        self.assertEqual(type(keys), list)

    def test_subscriptions(self):
        hub = octokit.Octokit()
        subscriptions = hub.users.subscriptions('irqed')
        self.assertEqual(type(subscriptions), list)
