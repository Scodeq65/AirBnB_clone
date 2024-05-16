#!/usr/bin/python3
"""Unit test for BaseModel."""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class."""

    def setUp(self):
        """Set up for each test methods."""
        self.model = BaseModel()

    def test_id_is_uuid(self):
        """Test that ID is a valid UUID."""
        self.assertIsInstance(self.model.id, str)
        try:
            uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is  not a valid UUID4")

    def test_created_at_is_datetime(self):
        """Test to confirm if created_at is datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test to confirm if updated_at is datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """Test the save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(
                model_dict["created_at"], self.model.created_at.isoformat()
        )
        self.assertEqual(
                model_dict["updated_at"], self.model.updated_at.isoformat()
        )
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
