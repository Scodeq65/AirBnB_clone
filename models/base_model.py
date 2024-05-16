#!/usr/bin/python3

"""BaseModel class which other sub class inherites from."""


import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique ID for each instances created.
        craeted_at (datetime): The time which an instance is created.
        updated_at (datetime): It shows the time an instance is updated.
    """

    def __init__(self):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns s atring rep of the instance.
        Returns:
            str: string representation in the format
                [<class name>] (<self.id>) <self.__dict__>"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attr updated_at
            with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all values of __dict__ of instance.
        Returns:
            dict: Dictionary rep of the instance with ISO format for datetime.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
