#!/usr/bin/python3
"""class BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModle"""
    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """str"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """save"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to dict"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__,
                          'created_at': self.created_at.isoformat(),
                           'updated_at': self.updated_at.isoformat()})
        return dictionary
