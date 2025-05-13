#!/usr/bin/env python3
"""Module 0-simple_helper_function
This module contains a helper function for calculating
start and end indexes for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and the end index (exclusive).
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
