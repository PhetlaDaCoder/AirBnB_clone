#!/usr/bin/python3
"""Unittest for the City class."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Defines tests for the City class."""

    def setUp(self):
        """Set up a new City instance before each test."""
        self.city = City()

    def test_instance_creation(self):
        """Test that a City instance is created."""
        self.assertIsInstance(self.city, City)

    def test_default_attributes(self):
        """Test default attributes of City."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.city.state_id = "1234"
        self.city.name = "Cape Town"
        self.assertEqual(self.city.state_id, "1234")
        self.assertEqual(self.city.name, "Cape Town")

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_to_dict_includes_attributes(self):
        """Test that state_id and name attributes are included in the dictionary."""
        self.city.state_id = "5678"
        self.city.name = "Durban"
        city_dict = self.city.to_dict()
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertEqual(city_dict["state_id"], "5678")
        self.assertEqual(city_dict["name"], "Durban")

    def test_string_representation(self):
        """Test the string representation of City."""
        string_rep = str(self.city)
        self.assertIn("[City]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
