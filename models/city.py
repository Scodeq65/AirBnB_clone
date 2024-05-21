#!/usr/bin/python3
"""City class that inherite form BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a review for a MySQL database.

    Inherit from BaseModel.
    Attributes:
        place_id (str): The place id.
        user_id (str): The User id.
        text (str): The text of the review
    """
    state_id = ""
    name = ""
