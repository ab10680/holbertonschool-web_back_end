#!/usr/bin/env python3
"""Module to measure the runtime of wait_n."""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure average execution time of wait_n.

    Args:
        n (int): number of concurrent tasks
        max_delay (int): maximum delay per task

    Returns:
        float: average execution time per task
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
