#!/usr/bin/env python3
"""Write a type-annotated function floor
    which takes a float n as argument and
    returns the floor of the float.
"""


def floor(n: float) -> int:
    """return value"""
    return int(n) if n >= 0 else int(n) - 1