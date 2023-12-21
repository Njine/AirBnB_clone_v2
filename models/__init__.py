#!/usr/bin/python3
"""Create a unique storage instance for your application."""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

# Constants for storage types
DB_STORAGE = "db"
FILE_STORAGE = "file"

# Get the value of HBNB_TYPE_STORAGE from the environment
storage_type = getenv("HBNB_TYPE_STORAGE", default=FILE_STORAGE)

# Create the storage instance based on the storage type
if storage_type == DB_STORAGE:
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage instance
storage.reload()
