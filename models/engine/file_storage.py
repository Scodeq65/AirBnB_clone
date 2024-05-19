#!/usr/bin/python3
"""
FileStorage module that helps to serialize and deserialize
BaseModel instances
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a json file and
    deserializes json file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns d dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serailizes __objects to the json file (path: __file_path)."""
        obj_dict = {
                key: obj.to_dict() for key,
                obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects file."""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
