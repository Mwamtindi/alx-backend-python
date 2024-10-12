#!/usr/bin/env python3
"""
A module with a type-annotated fxn floor to calculate floor of floating-point n
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The largest integer less than or equal to `n`.
    """
    return math.floor(n)
