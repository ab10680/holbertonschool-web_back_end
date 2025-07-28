#!/usr/bin/env python3
"""
This module contains a function that returns a tuple with a string and
the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A numeric value.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and
        the second is v squared (as float).
    """
    return (k, float(v ** 2))
