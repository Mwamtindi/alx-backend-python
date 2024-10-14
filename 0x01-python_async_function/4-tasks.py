#!/usr/bin/env python3
"""
A module that contains an asynchronous function to spawn multiple
task_wait_random calls.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay
    and return the delays in ascending order.

    Args:
        n : Number of times to spawn task_wait_random.
        max_delay : Maximum delay value to use for each task_wait_random call.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
