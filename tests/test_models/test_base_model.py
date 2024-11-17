#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from datetime import datetime
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class."""

    def test_init_with_kwargs(self):
        """Test instantiation with kwargs."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        base = BaseModel(id="1234", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "1234")
        self.assertEqual(base.created_at, dt)
        self.assertEqual(base.updated_at, dt)

    def test_init_without_kwargs(self):
        """Test instantiation without kwargs."""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)  # Check valid UUID
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertEqual(base.created_at, base.updated_at)

    def test_save_method(self):
        """Test the save method."""
        base = BaseModel()
        prev_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["id"], base.id)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["created_at"], base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], base.updated_at.isoformat())
        self.assertIsInstance(base_dict, dict)

    def test_str_method(self):
        """Test the __str__ method."""
        base = BaseModel()
        expected = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected)


if __name__ == "__main__":
    unittest.main()
