#!/usr/bin/env python3
"""
This module contains a function that returns a list of tuples containing
each element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of elements that support len().

    Returns:
        List[Tuple[Sequence, int]]: List of tuples (element, length).
    """
    return [(i, len(i)) for i in lst]
