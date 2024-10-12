#!/usr/bin/env python3
from typing import List

"""
A module that provides a function to sum a list of floating-point numbers.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floating-point numbers and returns the result.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
