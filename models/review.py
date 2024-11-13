#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review class.

    Attributes:
        place_id (string): The Place id.
        user_id (string): The User id.
        text (string): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
