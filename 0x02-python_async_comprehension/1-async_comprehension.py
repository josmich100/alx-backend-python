#!/usr/bin/env python3
'''
Module for 1-async_comprehension
'''


from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Returns a list of random float numbers
    '''
    return [i async for i in async_generator()]