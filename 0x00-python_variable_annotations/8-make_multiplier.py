#!/usr/bin/env python3
'''
This module contains the function make_multiplier that
returns a function that multiplies a float by a multiplier
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that multiplies a float by multiplier
    '''
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
