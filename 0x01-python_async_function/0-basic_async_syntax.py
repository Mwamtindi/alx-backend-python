#!/usr/bin/env python3
"""A Module containing an asynchronous function to wait for a random delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return delay.

    Args:
        max_delay : The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual number of seconds the coroutine waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
