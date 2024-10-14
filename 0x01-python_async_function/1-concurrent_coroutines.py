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
    work = [wait_random(max_delay) for _ in range(n)]
    outpt = await asyncio.gather(*work)
    return sorted(outpt)
