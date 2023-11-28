#!/usr/bin/python3
"""Module of matrix_divided function."""


def matrix_divided(matrix, div):
    """Division of all elements of a matrix.
    Args:
        matrix: must be a list of lists of integers or floats
        div: all elements of the  matrix divided by div, div is a number
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    m_int_f = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(print(m_int_f))
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(print(m_int_f))
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(print(m_int_f))
            if div == 0:
                raise ZeroDivisionError('division by zero')
    return list(map(lambda row:
                    list(map(lambda num: round(num / div, 2), row)), matrix))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
