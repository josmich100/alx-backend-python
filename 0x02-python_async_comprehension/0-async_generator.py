#!/usr/bin/env python3
'''
module for 0-async_generator
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Returns a generator of random float numbers
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)