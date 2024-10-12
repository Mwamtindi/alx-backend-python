#!/usr/bin/env python3
""" A module with a type-annotated function add """


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b
