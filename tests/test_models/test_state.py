#!/usr/bin/python3
"""Test for state class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test for State attributes."""

    def setUp(self):
        """Set up for each test."""
        self.state = State()

    def test_attributes(self):
        """Test that State has a name attribute and it's an empty string."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel."""
        self.assertIsInstance(self.state, State)


if __name__ == "__main__":
    unittest.main()
