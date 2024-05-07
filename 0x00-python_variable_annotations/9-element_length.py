#!/usr/bin/env python3
'''
This module contains the function element_length
that takes a list of strings and returns a
list of tuples with a string and its length
'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list of tuples with a string and its length
    '''
    return [(i, len(i)) for i in lst]
