#!/usr/bin/python3
"""FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import sys


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes to JSON"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes json"""
        try:
            with open(self.__file_path, "r") as f:

                for key, obj_dict in json.load(f).items():
                    obj_dict = getattr(
                        sys.modules[__name__], key.split(".")[0])(**obj_dict)
                    self.__objects[key] = obj_dict
        except FileNotFoundError:
            pass
