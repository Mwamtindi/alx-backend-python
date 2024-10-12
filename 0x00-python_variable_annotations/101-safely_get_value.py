#!/usr/bin/env python3
"""
Module that provides a function to safely get a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value for a given key from a dictionary.
    If the key is not present, returns the default value.

    Args:
        dct (Mapping[Any, Any]): A dictionary containing key-value pairs.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None]): The default value to return if
        the key is not found.

    Returns:
        Union[Any, T]: Value associated with the key,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
