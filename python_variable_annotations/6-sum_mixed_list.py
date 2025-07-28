#!/usr/bin/env python3
"""
This module contains a function that returns the sum
of a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of numbers.

    Returns:
        float: The sum of the list.
    """
    return sum(mxd_lst)
