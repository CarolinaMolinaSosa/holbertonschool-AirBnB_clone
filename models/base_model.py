#!/usr/bin/python3
"""class BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModle"""
    def __init__(self):
        """init"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str"""
        return(f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__,
                          'created_at': self.created_at.isoformat(),
                           'updated_at': self.updated_at.isoformat()})
        return dictionary
