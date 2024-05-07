#!/usr/bin/env python3
'''
This module contains the function safely_get_value
that takes a dictionary and a key and returns the
value of the key if it exists, otherwise None
'''


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    Returns the value of a key in a dictionary
    '''
    if key in dct:
        return dct[key]
    else:
        return default
