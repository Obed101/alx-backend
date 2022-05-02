#!/usr/bin/env python3
"""This module does a simple pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns a tuple of
    start and end index of the response
    """
    end = 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)
