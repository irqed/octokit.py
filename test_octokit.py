#!/usr/bin/env python
# encoding: utf-8

"""Tests for Octokit."""

import unittest

import octokit
import pytest


class AuthenticationTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        hub = octokit.Octokit(login='', password='')
        assert hub.basic_authenticated is True

    def test_token(self):
        hub = octokit.Octokit(access_token='', client_secret='')
        assert hub.basic_authenticated is False
        assert hub.token_authenticated is True

    def test_application(self):
        hub = octokit.Octokit(client_id='', client_secret='')
        assert hub.basic_authenticated is False
        assert hub.token_authenticated is False
        assert hub.application_authenticated is True

    def test_user(self):
        hub = octokit.Octokit(login='', password='')
        hub_two = octokit.Octokit(access_token='', client_secret='')

        assert hub.application_authenticated is False
        assert hub_two.application_authenticated is False

        assert hub.user_authenticated is True
        assert hub_two.user_authenticated is True
