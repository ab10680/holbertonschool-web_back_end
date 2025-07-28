#!/usr/bin/env python3
"""Module that defines an async comprehension to collect random numbers."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random floats from async_generator using async comprehension.

    Returns:
        List[float]: List of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
