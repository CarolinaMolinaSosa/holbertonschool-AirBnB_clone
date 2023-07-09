#!/usr/bin/python3
"""Tests for User class"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_first_name(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        user = User()
        self.assertEqual(user.last_name, "")

    def test_email(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_password(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_instance(self):
        user = User()
        self.assertIsInstance(user, type(User()))
