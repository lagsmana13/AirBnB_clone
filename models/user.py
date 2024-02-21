#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user object."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
