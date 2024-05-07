#!/usr/bin/env python3
'''
Tasks
'''


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
	'''
	Returns a list of tasks
	'''
	return [task_wait_random(max_delay) for _ in range(n)]
