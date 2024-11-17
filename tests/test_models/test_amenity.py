#!/usr/bin/python3
"""Unittest for the Amenity class."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines tests for the Amenity class."""

    def setUp(self):
        """Set up a new Amenity instance before each test."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test that an Amenity instance is created."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_default_attributes(self):
        """Test default attributes of Amenity."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_to_dict_includes_name(self):
        """Test that 'name' attribute is included in the dictionary."""
        self.amenity.name = "Gym"
        amenity_dict = self.amenity.to_dict()
        self.assertIn("name", amenity_dict)
        self.assertEqual(amenity_dict["name"], "Gym")

    def test_string_representation(self):
        """Test the string representation of Amenity."""
        string_rep = str(self.amenity)
        self.assertIn("[Amenity]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
