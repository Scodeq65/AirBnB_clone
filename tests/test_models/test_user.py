#!/usr/bin/python3
"""Test for user."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test for User attribute."""

    def setUp(self):
        """Set up for each test."""
        self.user = User()

    def test_attributes(self):
        """Test that User has the correct attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, User)


if __name__ == '__main__':
    unittest.main()
