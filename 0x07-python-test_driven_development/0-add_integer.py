#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: first int or float
        b: second int or float

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Returns: Sum of two numbers.
    """
    if ((type(a) not in (int, float))):
        raise TypeError("a must be an integer")
    if ((type(b) not in (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/import doctest.txt')