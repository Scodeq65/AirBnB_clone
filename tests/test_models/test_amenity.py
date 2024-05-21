#!/usrbin/python3
"""Test amenity class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test amenity instance."""

    def setUp(self):
        """Set up for each test."""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test that Amenity has a name attribute and it's an empty string."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertIsInstance(self.amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
