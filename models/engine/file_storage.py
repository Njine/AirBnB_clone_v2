#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone."""

import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format."""

    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of models currently in storage.

        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            for key, value in self.__objects.items():
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    dic[key] = value
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save storage dictionary to file."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Load storage dictionary from file."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                my_dict = json.load(f)
                for key, val in my_dict.items():
                    value = eval(val["__class__"])(**val)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete an existing element."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ Call reload()."""
        self.reload()
