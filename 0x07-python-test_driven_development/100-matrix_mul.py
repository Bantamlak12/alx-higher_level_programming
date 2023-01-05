#!/usr/bin/python3
"""A module that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of int/floats): The first matrix.
        m_b (list of lists of int/floats): The second matrix.

    Raises:
        TypeError: if either m_a or m_b is not a list.
        TypeError: if m_a or m_b is not a list of lists.
        TypeError: if one element m_a or m_b is not an integer or a float.
        TypeError: if m_a or m_b is not a rectangle.
        ValueError: if m_a or m_b is empty (it means: = [] or = [[]]).
        ValueError: if m_a and m_b can’t be multiplied.

    Returns:
        A new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError('m_a should contain only integers or floats')

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError('m_b should contain only integers or floats')

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Creating the matrix of dimension len(m_a) × len(m_b[0])
    # filling the matrix with 0 entries

    C = []
    for row in range(len(m_a)):
        curr_row = []
        for col in range(len(m_b[0])):
            curr_row.append(0)
        C.append(curr_row)

    # Performing the matrix multiplication

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            curr_val = 0
            for k in range(len(m_a[0])):
                curr_val += m_a[i][k] * m_b[k][j]
            C[i][j] = curr_val
    return C
