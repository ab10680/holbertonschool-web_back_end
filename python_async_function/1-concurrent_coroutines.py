#!/usr/bin/env python3
"""Coroutine that runs multiple wait_random coroutines concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the delays.

    Args:
        n (int): number of coroutines to spawn
        max_delay (int): maximum delay for each coroutine

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks: List[asyncio.Task] = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
