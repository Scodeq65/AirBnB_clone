#!/usr/bin/python3
"""City class that inherite form BaseModel."""

from models.base_model import BaseModel

class City(BaseModel):
    """Initialize city mothod."""
    state_id = ""
    name = ""
