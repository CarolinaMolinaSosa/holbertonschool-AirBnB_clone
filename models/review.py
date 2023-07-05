#!/usr/bin/python3
"""A class Review that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This is a Subclass"""
    place_id = ""
    user_id =  ""
    text = ""
