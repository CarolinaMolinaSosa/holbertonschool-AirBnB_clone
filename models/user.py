#!/usr/bin/python3
"""A class User that inherits form Basemodel"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is a Subclass"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
