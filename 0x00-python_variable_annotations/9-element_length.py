#!/usr/bin/env python3
"""
Module that provides a function to get the lengths of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): A list or iterable of sequences eg strs,lists

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        an element from `lst` and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
