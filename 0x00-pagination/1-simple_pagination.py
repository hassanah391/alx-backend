#!/usr/bin/env python3
"""Module 1-simple_pagination
This module implements a Server class that paginates a database
of popular baby names.
It demonstrates simple pagination techniques using
the index_range helper function
from the previous module to retrieve specific pages of data.
"""

import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """find the correct indexes to paginate the dataset correctly

        Args:
            page (int, optional): The current page number. Defaults to 1.
            page_size (int, optional): The number of items per page.
                Defaults to 10.

        Returns:
            List[List]: the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the dataset
        data = self.dataset()

        # Calculate the start and end indexes
        start_idx, end_idx = index_range(page, page_size)

        # Return an empty list if the start index exceeds the dataset length
        if start_idx >= len(self.__dataset):
            return []
        # Return the slice of the dataset corresponding
        # to the requested page
        return data[start_idx: end_idx]
