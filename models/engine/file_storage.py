import json
from models.base_model import BaseModel
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls:
            return {key: value for key, value in self.__objects.items() if key.split('.')[0] == cls.__name__}
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if isinstance(obj, BaseModel):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                loaded_data = json.load(f)
                for key, value in loaded_data.items():
                    class_name = value["__class__"]
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj and isinstance(obj, BaseModel):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """ calls reload()
        """
        self.reload()
