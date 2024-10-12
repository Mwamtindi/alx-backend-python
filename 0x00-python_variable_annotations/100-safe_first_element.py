#!/usr/bin/env python3
"""
Module that provides a function to safely get the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the 1st element of a sequence if it exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence (eg list,tuple) of any type of elements

    Returns:
        Union[Any, None]:1st element of the sequence if present, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
