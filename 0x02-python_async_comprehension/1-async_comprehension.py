#!/usr/bin/env python3
"""A module with Async comprehension that collects 10 random numbers."""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random nums using async comprehension over async_generator"""
    return [i async for i in async_generator()]
