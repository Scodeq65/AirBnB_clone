#!/usr/bin/python3
"""Unit test for BaseModel class."""

import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseMdel class."""

    def test_init(self):
        """Test the initialization of BaseModel instances."""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))
        self.assertTrue(obj.updated_at - obj.created_at < timedelta(seconds=1))

    def test_str_method(self):
        """Test the __str__ method."""
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Test the save method."""
        obj = BaseModel()
        first_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(first_updated_at, obj.updated_at)

    def test_to_dict(self):
        """Test instantiation from dictionary."""
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['name'], "My First Model")
        self.assertEqual(obj_dict['my_number'], 89)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_kwargs(self):
        """Test initialization with kwargs."""
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)

        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)
        self.assertEqual(new_obj.name, obj.name)
        self.assertEqual(new_obj.my_number, obj.my_number)


if __name__ == '__main__':
    unittest.main()
