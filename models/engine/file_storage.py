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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded = json.load(file)
            self.__objects = {}
            for key, value in loaded.items():
                key_class = key.split(".")[0]
                self.__objects[key] = self.classes[key_class](**value)
