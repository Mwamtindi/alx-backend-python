#!/usr/bin/env python3
"""
Module that  provides a function that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a func that multiplies a given float by the specified multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float as an argument
        and returns the product of that float and the multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
