#!/usr/bin/env python3
"""ALX SE"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size 2 containing a start and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)
