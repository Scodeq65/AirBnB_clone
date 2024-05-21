#!/usr/bin/python3
"""Creates review method,"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review for a MySQL database.

    Inherits from BaseModel.
    Attributes:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
