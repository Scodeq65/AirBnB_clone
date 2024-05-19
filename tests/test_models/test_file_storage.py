#!/usr/bin/python3
"""Unittests for FileStorage."""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up for tests."""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all(self):
        """Test the all method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
