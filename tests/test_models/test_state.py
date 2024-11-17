#!/usr/bin/python3
"""Unittest for the State class."""
import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Defines tests for the State class."""

    def setUp(self):
        """Set up a new State instance before each test."""
        self.state = State()

    def test_instance_creation(self):
        """Test that a State instance is created."""
        self.assertIsInstance(self.state, State)

    def test_default_attributes(self):
        """Test default attributes of State."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_to_dict_includes_attributes(self):
        """Test that all attributes are included in the dictionary."""
        self.state.name = "New York"
        state_dict = self.state.to_dict()
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "New York")

    def test_string_representation(self):
        """Test the string representation of State."""
        string_rep = str(self.state)
        self.assertIn("[State]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
