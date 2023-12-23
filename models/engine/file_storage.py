#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    _file_path = 'file.json'

    def __init__(self):
        self._objects = {}  # Dictionary to store objects

    def all(self, cls=None):
        """
        Retrieve all objects or objects of a specific class.

        Args:
            cls (class, optional): The class type to filter objects. Defaults to None.

        Returns:
            dict: Dictionary of objects.
        """
        if cls is None:
            return self._objects
        cls_name = cls.__name__
        return {key: obj for key, obj in self._objects.items() if key.split('.')[0] == cls_name}

    def new(self, obj):
        """
        Add a new object to storage.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj

    def save(self):
        """
        Save objects to a JSON file.
        """
        with open(FileStorage._file_path, 'w') as f:
            # Serialize objects to JSON
            serialized_objects = {key: obj.to_dict() for key, obj in self._objects.items()}
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Load objects from a JSON file.
        """
        try:
            with open(FileStorage._file_path, 'r') as f:
                # Deserialize objects from JSON
                serialized_objects = json.load(f)
                self._objects = {key: classes[val['__class__']](**val) for key, val in serialized_objects.items()}
        except FileNotFoundError:
            print("File not found. Skipping reload.")

    def delete(self, obj=None):
        """
        Delete the specified object from storage.

        Args:
            obj: The object to be deleted.
        """
        if obj:
            obj_key = f"{obj.__class__.__name__}.{obj.id}"
            self._objects.pop(obj_key, None)
