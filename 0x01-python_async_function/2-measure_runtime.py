#!/usr/bin/env python3
'''
Measure the runtime
'''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
	'''
	Returns the time of execution
	'''
	start = time.time()
	asyncio.run(wait_n(n, max_delay))
	end = time.time()
	return (end - start) / n