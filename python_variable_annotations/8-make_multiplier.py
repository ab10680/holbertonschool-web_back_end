#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier factor.

    Returns:
        Callable[[float], float]: A function that multiplies a float.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
