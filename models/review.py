#!/usr/bin/python3
"""Creates review method,"""

from models.base_model import BaseModel


class Review(Basemodel):
    """Initialize review method."""
    place_id = ""
    user_id = ""
    text = ""
