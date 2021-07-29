#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
    def safe_first_element(lst):
        if lst:
            return lst[0]
        else:
            return None
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst"""
    if lst:
        return lst[0]
    else:
        return None