#!/usr/bin/python3
"""Unittests for FileStorage."""

import unittest
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up for tests."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Test the new method."""
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.assertTrue("User." + user.id in self.storage.all())
        self.assertTrue("Place." + place.id in self.storage.all())
        self.assertTrue("State." + state.id in self.storage.all())
        self.assertTrue("City." + city.id in self.storage.all())
        self.assertTrue("Amenity." + amenity.id in self.storage.all())
        self.assertTrue("Review." + review.id in self.storage.all())

    def test_save_reload(self):
        """Test the save method."""
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.storage.save()
        self.storage.reload()

        self.assertTrue("User." + user.id in self.storage.all())
        self.assertTrue("Place." + place.id in self.storage.all())
        self.assertTrue("State." + state.id in self.storage.all())
        self.assertTrue("City." + city.id in self.storage.all())
        self.assertTrue("Amenity." + amenity.id in self.storage.all())
        self.assertTrue("Review." + review.id in self.storage.all())


if __name__ == '__main__':
    unittest.main()
