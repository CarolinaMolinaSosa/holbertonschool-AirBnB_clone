#!/usr/bin/python3
"""A class City that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """This is a Subclass"""
    state_id = ""
    name = ""
