#!/usr/bin/env python3
"""Measure total runtime for executing async comprehensions in parallel."""

import asyncio
import time
from typing import Awaitable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure time to run async_comprehension 4 times in parallel.

    Returns:
        float: Total elapsed time in seconds.
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
