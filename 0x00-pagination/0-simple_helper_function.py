#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes in 2 integer arguments and returns a tuple of size two containing
    the start and end index corresponding to the range of indexes to
    return in a list for those pagination parameters
    Args:
        page(int): page number to return (1-indexed)
        page_size(int): numberof items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
