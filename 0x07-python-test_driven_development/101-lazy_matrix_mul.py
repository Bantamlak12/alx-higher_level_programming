#!/usr/bin/python3
"""A module that multiplies 2 matrices"""

import numpy as np
"""Importing library"""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices

    Args:
        m_a (list of lists of int/floats): The first matrix.
        m_b (list of lists of int/floats): The second matrix.

    Returns:
        a new matrix
    """

    return np.matmul(m_a, m_b)
