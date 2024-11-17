#!/usr/bin/python3
"""Unittest for the Place class."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines tests for the Place class."""

    def setUp(self):
        """Set up a new Place instance before each test."""
        self.place = Place()

    def test_instance_creation(self):
        """Test that a Place instance is created."""
        self.assertIsInstance(self.place, Place)

    def test_default_attributes(self):
        """Test default attributes of Place."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Luxury Villa"
        self.place.description = "A beautiful luxury villa."
        self.place.number_rooms = 5
        self.place.number_bathrooms = 3
        self.place.max_guest = 10
        self.place.price_by_night = 500
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Luxury Villa")
        self.assertEqual(self.place.description, "A beautiful luxury villa.")
        self.assertEqual(self.place.number_rooms, 5)
        self.assertEqual(self.place.number_bathrooms, 3)
        self.assertEqual(self.place.max_guest, 10)
        self.assertEqual(self.place.price_by_night, 500)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_to_dict_includes_attributes(self):
        """Test that all attributes are included in the dictionary."""
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Penthouse"
        self.place.description = "A luxurious penthouse."
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 1000
        self.place.latitude = 34.0522
        self.place.longitude = -118.2437
        self.place.amenity_ids = ["amenity1"]

        place_dict = self.place.to_dict()
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenity_ids", place_dict)
        self.assertEqual(place_dict["city_id"], "1234")
        self.assertEqual(place_dict["user_id"], "5678")
        self.assertEqual(place_dict["name"], "Penthouse")
        self.assertEqual(place_dict["description"], "A luxurious penthouse.")
        self.assertEqual(place_dict["number_rooms"], 3)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 6)
        self.assertEqual(place_dict["price_by_night"], 1000)
        self.assertEqual(place_dict["latitude"], 34.0522)
        self.assertEqual(place_dict["longitude"], -118.2437)
        self.assertEqual(place_dict["amenity_ids"], ["amenity1"])

    def test_string_representation(self):
        """Test the string representation of Place."""
        string_rep = str(self.place)
        self.assertIn("[Place]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
