#!/usr/bin/python3
"""Unittest for HBNBCommand class"""

import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Clean up storage after tests"""
        storage.all().clear()

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.cmd.onecmd("quit"))
            self.assertIn(
                    "Exiting... Goodbye!", mock_stdout.getvalue().strip())

    def test_eof(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.cmd.onecmd("EOF"))
            self.assertIn(
                    "Exiting... Goodbye!", mock_stdout.getvalue().strip())

    def test_emptyline(self):
        """Test handling of empty line"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.cmd.onecmd("")
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)  # Should return an ID
            obj_id = output
            self.assertIn(f"BaseModel.{obj_id}", storage.all())

    def test_show(self):
        """Test the show command"""
        new_obj = BaseModel()
        new_obj.save()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.cmd.onecmd(f"show BaseModel {new_obj.id}")
            self.assertIn(str(new_obj), mock_stdout.getvalue().strip())

    def test_destroy(self):
        """Test the destroy command"""
        new_obj = BaseModel()
        new_obj.save()
        self.assertIn(f"BaseModel.{new_obj.id}", storage.all())
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.cmd.onecmd(f"destroy BaseModel {new_obj.id}")
            self.assertNotIn(f"BaseModel.{new_obj.id}", storage.all())

    def test_all(self):
        """Test the all command"""
        new_obj1 = BaseModel()
        new_obj1.save()
        new_obj2 = BaseModel()
        new_obj2.save()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.cmd.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(new_obj1), output)
            self.assertIn(str(new_obj2), output)

    def test_update(self):
        """Test the update command"""
        new_obj = BaseModel()
        new_obj.save()

        with patch('sys.stdout', new=StringIO()):
            self.cmd.onecmd(f'update BaseModel {new_obj.id} name "Test Name"')
            updated_obj = storage.all()[f"BaseModel.{new_obj.id}"]
            self.assertEqual(updated_obj.name, "Test Name")

        with patch('sys.stdout', new=StringIo()):
            self.cmd.onecmd(f'update BaseModel {new_obj.id} age 25')
            updated_obj = storage.all()[f"BaseModel.{new_obj.id}"]
            self.assertEqual(updated_obj.age, 25)


if __name__ == "__main__":
    unittest.main()
