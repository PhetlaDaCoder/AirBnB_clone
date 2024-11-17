#!/usr/bin/python3
"""Unittest for the User class."""
import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Defines tests for the User class."""

    def setUp(self):
        """Set up a new User instance before each test."""
        self.user = User()

    def test_instance_creation(self):
        """Test that a User instance is created."""
        self.assertIsInstance(self.user, User)

    def test_default_attributes(self):
        """Test default attributes of User."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.user.email = "test@example.com"
        self.user.password = "securepassword"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_to_dict_includes_attributes(self):
        """Test that all attributes are included in the dictionary."""
        self.user.email = "test@example.com"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        
        self.assertIn("email", user_dict)
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertIn("first_name", user_dict)
        self.assertEqual(user_dict["first_name"], "John")
        self.assertIn("last_name", user_dict)
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_string_representation(self):
        """Test the string representation of User."""
        string_rep = str(self.user)
        self.assertIn("[User]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
