#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position.

        Args:
            size: The size of the square (default is 0).
            position: The position of the square as a tuple (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is bool or not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            The position of the square as a tuple.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: The new position value as a tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or 
            len(value) != 2 or
            type(value[0]) is bool or
            type(value[1]) is bool or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        If size is 0, print an empty line.
        position[0] is used for horizontal offset (spaces before #).
        position[1] is used for vertical offset (empty lines before square).
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
