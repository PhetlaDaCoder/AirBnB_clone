import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from hbnb import HBNBCommand  # Assuming your command file is named 'hbnb.py'


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test the quit command."""
        cmd = HBNBCommand()
        result = cmd.onecmd('quit')
        self.assertTrue(result)  # Expects True to exit the loop
        self.assertIn("Exiting... Goodbye!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test the EOF command (Ctrl+D)."""
        cmd = HBNBCommand()
        result = cmd.onecmd('EOF')
        self.assertTrue(result)
        self.assertIn("Exiting... Goodbye!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class(self, mock_stdout):
        """Test create with no class name."""
        cmd = HBNBCommand()
        cmd.onecmd('create')
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class(self, mock_stdout):
        """Test create with an invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd('create FakeClass')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('models.storage', autospec=True)
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_valid(self, mock_stdout, mock_storage):
        """Test create with a valid class name."""
        cmd = HBNBCommand()
        with patch.object(BaseModel, 'save', return_value=None):
            cmd.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Output should be a non-empty ID

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_missing_class(self, mock_stdout):
        """Test show with missing class name."""
        cmd = HBNBCommand()
        cmd.onecmd('show')
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_invalid_class(self, mock_stdout):
        """Test show with an invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd('show FakeClass 1234')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_missing_instance_id(self, mock_stdout):
        """Test show with missing instance id."""
        cmd = HBNBCommand()
        cmd.onecmd('show BaseModel')
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('models.storage.all', return_value={})
    def test_do_show_no_instance(self, mock_storage, mock_stdout):
        """Test show with no instance found."""
        cmd = HBNBCommand()
        cmd.onecmd('show BaseModel 1234')
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('models.storage.all', return_value={})
    def test_do_all_empty(self, mock_storage, mock_stdout):
        """Test all with no instances."""
        cmd = HBNBCommand()
        cmd.onecmd('all')
        self.assertIn("[]", mock_stdout.getvalue())  # Should output empty list

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_invalid_class(self, mock_stdout):
        """Test all with an invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd('all FakeClass')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_missing_class(self, mock_stdout):
        """Test update with missing class name."""
        cmd = HBNBCommand()
        cmd.onecmd('update')
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_invalid_class(self, mock_stdout):
        """Test update with an invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd('update FakeClass 1234 name "John"')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('models.storage.all', return_value={})
    def test_do_update_no_instance(self, mock_storage, mock_stdout):
        """Test update with no instance found."""
        cmd = HBNBCommand()
        cmd.onecmd('update BaseModel 1234 name "John"')
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('models.storage.all', return_value={'BaseModel.1234': BaseModel()})
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_valid(self, mock_stdout, mock_storage):
        """Test update with valid inputs."""
        cmd = HBNBCommand()
        cmd.onecmd('update BaseModel 1234 name "John"')
        self.assertNotIn("** invalid attribute name **", mock_stdout.getvalue())
        # You could also verify that the instance's attribute was updated if needed.

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_missing_class(self, mock_stdout):
        """Test destroy with missing class name."""
        cmd = HBNBCommand()
        cmd.onecmd('destroy')
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_invalid_class(self, mock_stdout):
        """Test destroy with an invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd('destroy FakeClass 1234')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('models.storage.all', return_value={'BaseModel.1234': BaseModel()})
    @patch('models.storage.delete')
    def test_do_destroy_valid(self, mock_delete, mock_storage, mock_stdout):
        """Test destroy with a valid class and instance."""
        cmd = HBNBCommand()
        cmd.onecmd('destroy BaseModel 1234')
        mock_delete.assert_called_once_with('BaseModel.1234')
        self.assertIn("Instance deleted", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
