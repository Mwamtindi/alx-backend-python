#!/usr/bin/env python3
""" A moduule with measure_runtime coroutine that will execute async_comp """

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ A funtion Measure Runtime to execute async_comp 4 times in parallel """
    fst = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    lst = asyncio.get_event_loop().time()
    return lst - fst
