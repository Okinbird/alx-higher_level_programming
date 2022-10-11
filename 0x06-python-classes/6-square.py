#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): position of the square in 2D space
        Returns:
            None
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """getter of __size
         Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
