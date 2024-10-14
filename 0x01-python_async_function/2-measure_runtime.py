#!/usr/bin/env python3
"""
A module that  measure the runtime of an asynchronous function.
"""

import time
import asyncio
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken to execute wait_n(n, max_delay).
    Args:
        n : The number of calls to wait_random.
        max_delay : The maximum delay for each call to wait_random.

    Returns:
        float: The average time per call (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
