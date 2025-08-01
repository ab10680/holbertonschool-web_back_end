#!/usr/bin/env python3
"""Async Generator that yields random floats between 0 and 10."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random floats between 0 and 10.

    Yields:
        float: Random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
