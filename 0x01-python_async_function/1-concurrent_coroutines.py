#!/usr/bin/env python3
"""
A Module containing an asynchronous func that spawns multiple wait_random calls
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n : Number of times to spawn wait_random.
        max_delay : Maximum delay value to use for each wait_random call.

    Returns:
        List: List of delay times in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
