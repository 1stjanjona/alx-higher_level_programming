#!/usr/bin/python3
"""Lazy matrix"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplication of 2 matricies
    Args:
        m_a: input of 1st matrix
        m_b: input of 2nd matrix
    """
    return numpy.matmul(m_a, m_b)
