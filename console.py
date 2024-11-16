#!/usr/bin/python3
"""Defines the HBNBCommand."""

import cmd
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
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
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
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
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
        if not storage.get(instance_key):
            print("** no instance found **")
            return
        storage.delete(instance_key)
        print("Instance deleted")

    def do_all(self, arg):
        """Prints all string representations of instances.

        Args:
            arg (str): The class name (optional).
        """
        if arg and arg not in self.__classes:
            print("** class doesn't exist **")
            return
        instances = storage.all(arg) if arg else storage.all()
        print([str(inst) for inst in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on class name, id, and
        attribute name/value."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = f"{args[0]}.{args[1]}"
        instance = storage.get(instance_key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            attr_value = attr_value.strip('"')

        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
