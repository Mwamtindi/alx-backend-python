#!/usr/bin/env python3
"""
Module provides a function to sum a list of integers and floating-point num-s.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of int-s and floating-point num-s and returns result as float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing int-s and floats.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
