#!/usr/bin/env python
# encoding: utf-8

"""Tests for Octokit."""

import unittest

import octokit
import pytest


class AuthenticationTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_unauthenticated(self):
        hub = octokit.Octokit()
        assert hub.authenticated is False

    def test_basic(self):
        hub = octokit.Octokit(login='', password='')
        assert hub.authenticated is True
        assert hub.basic_authenticated is True

    def test_token(self):
        hub = octokit.Octokit(access_token='', client_secret='')
        assert hub.basic_authenticated is False

        assert hub.authenticated is True
        assert hub.token_authenticated is True

    def test_application(self):
        hub = octokit.Octokit(client_id='', client_secret='')
        assert hub.basic_authenticated is False
        assert hub.token_authenticated is False

        assert hub.authenticated is True
        assert hub.application_authenticated is True

    def test_user(self):
        hub = octokit.Octokit(login='', password='')
        hub_two = octokit.Octokit(access_token='', client_secret='')
        assert hub.application_authenticated is False
        assert hub_two.application_authenticated is False

        assert hub.user_authenticated is True
        assert hub_two.user_authenticated is True

        assert hub.authenticated is True
        assert hub_two.authenticated is True


class UserTestCase(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_user(self):
        user = octokit.Octokit(login='', password='').user
        assert user.name == ''

    def test_another_user(self):
        hub = octokit.Octokit(login='', password='')
        assert hub.users['username'].name == ''

    def test_users(self):
        users = octokit.Octokit(login='', password='').users
        assert len(users) == 100
        assert len(users.next()) == 100  # get the second page of the results
