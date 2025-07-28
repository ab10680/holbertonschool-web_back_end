#!/usr/bin/env python3
"""Module to measure total runtime of parallel async comprehensions."""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total execution time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
