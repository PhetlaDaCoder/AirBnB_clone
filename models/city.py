#!/usr/bin/python3
"""Defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class representation.

    Attributes:
       state_id (string): The state id
       name (string): Name of the city.
    """

    state_id = ""
    name = ""
