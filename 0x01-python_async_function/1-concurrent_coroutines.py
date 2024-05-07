#!/usr/bin/env python3
'''
Concurrent Coroutines
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
	'''
	Returns a list of delays
	'''
	delays = [wait_random(max_delay) for _ in range(n)]
	return [await delay for delay in asyncio.as_completed(delays)]
