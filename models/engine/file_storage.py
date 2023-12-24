#!/usr/bin/python3
import json
import shlex  # Import shlex module for string splitting

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    def __init__(self, file_path="file.json"):
        """Initialize FileStorage with a file path."""
        self.__file_path = file_path
        self.__objects = {}

    # Map class names to corresponding classes
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def all(self, cls=None):
        """Returns a dictionary of objects filtered by class.
        
        Args:
            cls (type): Class type for filtering objects.
            
        Returns:
            dict: Dictionary of objects.
        """
        dic = {}
        if cls:
            for key in self.__objects:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition and partition[0] == cls.__name__:
                    dic[key] = self.__objects[key]
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """Sets __objects to given obj.
        
        Args:
            obj: Given object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize instances to the JSON file."""
        my_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize JSON file to instances."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name = value.get('__class__')
                    if class_name in self.CLASSES:
                        cls = self.CLASSES[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            print(f"File {self.__file_path} not found. Creating a new one.")

    def delete(self, obj=None):
        """Delete an existing element."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Calls reload."""
        self.reload()
