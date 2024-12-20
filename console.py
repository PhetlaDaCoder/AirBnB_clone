#!/usr/bin/python
"""Defines the HBNBCommand."""

import cmd
import re
import shlex
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Defines the HBNBCommand command interpreter.

    Attributes:
        prompt (string): The command prompt.
    """

    prompt = '(hbnb)'
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City":  City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting... Goodbye!")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)."""
        print("Exiting... Goodbye!")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return

        new_instance = self.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("**  class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        instance = storage.get(instance_key)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        instance = storage.get(instance_key)
        if instance:
            storage.delete(instance_key)
            print("Instance deleted")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances.

        Args:
            arg (str): The class name (optional).
        """
        if arg and arg not in self.__classes:
            print("** class doesn't exist**")
            return

        instances = storage.all(arg) if arg else storage.all()
        print([str(instance) for instance in instances.values()])

    def do_update(self, args):
        """Updates an instance based on class name, id, and
        attribute name/value."""
        args = shlex.split(args)

        if len(args) < 4:
            print("** instance id missing **")
            return

        class_name, obj_id, attr_name, attr_value = (
                args[0], args[1], args[2], args[3]
                )
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif attr_value.replace(".", "", 1).isdigit():
                attr_value = float(attr_value)
            else:
                attr_value = attr_value.strip('"').strip("'")
        except ValueError:
            pass

        if not hasattr(obj, attr_name):
            print(f"** invalid attribute name **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()
        print(f"{class_name} instance {obj_id} updated")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
