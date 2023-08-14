"""
Factorial Module

This module provides a function to calculate the factorial of a given non-negative integer.
"""


def factorial(num):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        num (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the input integer.
    """
    if num == 0:
        return 1
    return num * factorial(num - 1)
