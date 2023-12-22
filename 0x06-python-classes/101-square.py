#!/usr/bin/python3
"""Defines a class Square.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.size == 0:
            return ''
        r = ''
        for i in range(self.position[1]):
            r += '\n'
        for i in range(self.size):
            r += (' ' * self.position[0]) + ("#" * self.size) + '\n'
        return r[:-1]

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        print(str(self))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if value[0] < 0 or value[1] < 0:
                raise Exception()
        except Exception:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
