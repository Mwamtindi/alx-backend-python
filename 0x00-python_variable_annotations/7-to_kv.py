#!/usr/bin/env python3
"""
A module provides a func that returns a tuple with string and the sq of number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a num (int or float) and returns a tuple.
    The 1st element is the str `k`, and 2nd is the sq of the num `v` as float.

    Args:
        k (str): A string.
        v (Union[int, float]): A number (integer or float).

    Returns:
        Tuple[str, float]: Tuple where the 1st element is `k`
        and 2nd element is the sq of `v`.
    """
    return (k, float(v ** 2))
