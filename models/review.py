#!/usr/bin/python3
"""This module defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a review object."""

    place_id = ""
    user_id = ""
    text = ""
