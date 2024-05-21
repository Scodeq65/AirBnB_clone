#!/usr/bin/python3
"""Test for city class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test city attributes."""

    def setUp(self):
        """Set up for each test."""
        self.city = City()

    def test_attributes(self):
        """Test that City has the correct attributes."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test that City is a subclass of BaseModel."""
        self.assertIsInstance(self.city, City)


if __name__ == "__main__":
    unittest.main()
