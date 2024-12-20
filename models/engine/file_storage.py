#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents a storage engine.

    Attributes:
        __file_path (string): Name of the file  to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Prints all string representations of instances.

        Args:
            cls (string): The class name (optional).

        Returns:
            dict: A dicyionary of objects
        """
        if cls:
            return {key: obj for key, obj in self.__objects.items()
                    if obj.__class__.__name__ == cls}
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {key: obj.to_dict() for key, obj in odict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(class_map[cls_name](**o))
        except FileNotFoundError:
            pass

    def get(self, key):
        """Gets an object by its key.

        Args:
            key (str): The key of the object to get.

        Returns:
            The object if found, otherwise None.
        """
        return self.__objects.get(key)

    def delete(self, obj=None):
        """Deletes object from __objects, if it exists.

        Args:
            obj (objects): The object to delete.
        """
        if obj:
            if isinstance(obj, str):
                key = obj
            else:
                key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
