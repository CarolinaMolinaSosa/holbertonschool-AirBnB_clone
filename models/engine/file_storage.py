#!/usr/bin/python3
"""FileStorage"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj with key"""
        key = f"{obj.__class__.__name__}.{id}"
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
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
