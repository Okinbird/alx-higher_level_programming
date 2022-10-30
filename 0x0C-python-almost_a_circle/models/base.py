#!/usr/bin/python3
"""
    Defines a Base model class with an id attributes
    to avoid duplicating the same code
"""


class Base:
    """The base class

    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
