#!/usr/bin/env python3
"""
Module that provides a func to zoom into an array by repeating
elements a specified number of times.
"""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list where each element in input tuple is repeated `factor` times

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The number of times to repeat each element.

    Returns:
        List[int]: A list with each element repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
