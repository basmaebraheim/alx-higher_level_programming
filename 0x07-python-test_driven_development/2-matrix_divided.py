#!/usr/bin/python3

def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix: matrix to devide its elements
        div: number to devide matrix element by

    Raises:
        ZeroDivisionError: if div equal 0.
        TypeError: if div not a number.
        TypeError: matrix is not a list of numbers.
        TypeError: not each row of the matrix must have the same size. 
        TypeError: any element in matrix is not number. 

    Returns: Sum of two numbers.
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
