#!/usr/bin/python3
"""Creates review method,"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Initialize review method."""
    place_id = ""
    user_id = ""
    text = ""
