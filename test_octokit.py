#!/usr/bin/env python
# encoding: utf-8

"""Tests for Octokit."""

import os
import pytest
import unittest

import octokit


class AuthenticationTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_unauthenticated(self):
        hub = octokit.Octokit()
        self.assertEqual(hub.authenticated, False)

    def test_basic(self):
        login = os.environ.get('OCTOKIT_LOGIN')
        password = os.environ.get('OCTOKIT_PASSWORD')

        hub = octokit.Octokit(login=login, password=password)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.basic_authenticated, True)

    def test_token(self):
        hub = octokit.Octokit(access_token='', client_secret='')

        self.assertEqual(hub.basic_authenticated, False)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.token_authenticated, True)

    def test_application(self):
        hub = octokit.Octokit(client_id='', client_secret='')

        self.assertEqual(hub.basic_authenticated, False)
        self.assertEqual(hub.token_authenticated, False)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub.application_authenticated, True)

    def test_user(self):
        hub = octokit.Octokit(login='', password='')
        hub_two = octokit.Octokit(access_token='', client_secret='')

        self.assertEqual(hub.application_authenticated, False)
        self.assertEqual(hub_two.application_authenticated, False)

        self.assertEqual(hub.authenticated, True)
        self.assertEqual(hub_two.authenticated, True)

        self.assertEqual(hub.user_authenticated, True)
        self.assertEqual(hub_two.user_authenticated, True)
