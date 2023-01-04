#!/usr/bin/python3
"""A module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """"
    Args:
        matrix: must be a list of lists of integers or floats,
                otherwise raise a TypeError exception.

                each row of the matrix must be of the same size,
                otherwise raise a TypeError exception.

        div: must be a number(integer or float), otherwise raise a
             TypeError exception.

             div can't be equal to 0, otherwise raise a ZeroDivisionError
             exception.
    Returns:
        a new matrix
   """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
