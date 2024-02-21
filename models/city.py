#!/usr/bin/python3
"""This module defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city object."""

    state_id = ""
    name = ""
