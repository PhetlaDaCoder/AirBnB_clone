#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from datetime import datetime
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review




class TestFileStorage(unittest.TestCase):
    """Defines unittests for the FileStorage class."""

    def setUp(self):
        """Set up resources for tests."""
        self.storage = FileStorage()
        self.base = BaseModel()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up resources after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """Test the all method."""
        self.storage.new(self.base)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.base.id}", all_objects)
        self.assertEqual(all_objects[f"BaseModel.{self.base.id}"], self.base)

    def test_new_method(self):
        """Test the new method."""
        self.storage.new(self.base)
        key = f"BaseModel.{self.base.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.base)

    def test_save_and_reload_methods(self):
        """Test the save and reload methods."""
        self.storage.new(self.base)
        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "r") as file:
            file_data = json.load(file)
        self.assertIn(f"BaseModel.{self.base.id}", file_data)

        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.base.id}", all_objects)
        self.assertIsInstance(all_objects[f"BaseModel.{self.base.id}"], BaseModel)

    def test_delete_method(self):
        """Test the delete method."""
        self.storage.new(self.base)
        key = f"BaseModel.{self.base.id}"
        self.assertIn(key, self.storage.all())

        self.storage.delete(self.base)
        self.assertNotIn(key, self.storage.all())

        self.storage.new(self.base)

        self.storage.delete(key)
        self.assertNotIn(key, self.storage.all())

    def test_get_method(self):
        """Test the get method."""
        self.storage.new(self.base)
        key = f"BaseModel.{self.base.id}"
        obj = self.storage.get(key)
        self.assertEqual(obj, self.base)

    def test_all_with_class(self):
        """Test the all method with a class filter."""
        another_base = BaseModel()
        self.storage.new(self.base)
        self.storage.new(another_base)

        filtered_objects = self.storage.all("BaseModel")
        self.assertIn(f"BaseModel.{self.base.id}", filtered_objects)
        self.assertIn(f"BaseModel.{another_base.id}", filtered_objects)
        non_existing = self.storage.all("NonExistentClass")
        self.assertEqual(non_existing, {})


if __name__ == "__main__":
    unittest.main()
