#!/usr/bin/env python3
"""Module that provides a function returning an asyncio.Task."""

import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random with given delay.

    Args:
        max_delay (int): The maximum delay to pass to wait_random

    Returns:
        asyncio.Task: A task that wraps wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
