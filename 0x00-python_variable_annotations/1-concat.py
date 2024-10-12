#!/usr/bin/env python3
""" A module with a type -annotated function concat to concatenate 2 strs """


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string formed by joining `str1` and `str2`.
    """
    return str1 + str2
