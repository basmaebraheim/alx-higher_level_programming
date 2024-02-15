#!/usr/bin/python3

def print_square(size):
    """prints a square with the character #

    Args:
        size: is the size length of the square

    Raises: 
        TypeError: size is not int.
        TypeError: size is float. 
        ValueError: size less than 0.

    Returns: My name is <first name> <last name>.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, int(size)):
        for j in range(0, int(size)):
            print("#", end="")
        print("")


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
