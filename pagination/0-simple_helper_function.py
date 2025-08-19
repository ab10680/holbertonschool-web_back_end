#!/usr/bin/env python3
"""
Helper to compute start and end indexes for paginating a sequence.

Given a 1-based page number and a page size, this module exposes the
`index_range` function which returns a (start, end) tuple suitable for
slicing a list (start inclusive, end exclusive).
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end index for pagination.

    Args:
        page: 1-based page number (>= 1).
        page_size: number of items per page (>= 1).

    Returns:
        A tuple (start, end) for slicing, where:
        - start is inclusive
        - end is exclusive
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
