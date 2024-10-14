#!/usr/bin/env python3
"""
A module that create an asyncio.Task from wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: A Task object that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
