#!/usr/bin/python3
"""Unittest for the Review class."""
import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines tests for the Review class."""

    def setUp(self):
        """Set up a new Review instance before each test."""
        self.review = Review()

    def test_instance_creation(self):
        """Test that a Review instance is created."""
        self.assertIsInstance(self.review, Review)

    def test_default_attributes(self):
        """Test default attributes of Review."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        """Test setting attributes."""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "This is a great place to stay!"

        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "This is a great place to stay!")

    def test_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_to_dict_includes_attributes(self):
        """Test that all attributes are included in the dictionary."""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "Amazing experience!"

        review_dict = self.review.to_dict()
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertEqual(review_dict["place_id"], "1234")
        self.assertEqual(review_dict["user_id"], "5678")
        self.assertEqual(review_dict["text"], "Amazing experience!")

    def test_string_representation(self):
        """Test the string representation of Review."""
        string_rep = str(self.review)
        self.assertIn("[Review]", string_rep)
        self.assertIn("id", string_rep)
        self.assertIn("created_at", string_rep)
        self.assertIn("updated_at", string_rep)


if __name__ == "__main__":
    unittest.main()
