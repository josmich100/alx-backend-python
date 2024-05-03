#!/usr/bin/env python3
'''
This module contains the function 
safe_first_element that takes a list 
of any type and returns the first element 
of the list if it exists, otherwise None
'''


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Returns the first element of a list
    '''
    if lst:
        return lst[0]
    else:
        return None
