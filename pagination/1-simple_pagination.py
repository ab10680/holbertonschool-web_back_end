#!/usr/bin/env python3
"""
Simple pagination for a CSV dataset of popular baby names.

This module provides an index_range helper and a Server class that
exposes a get_page method to return a paginated slice of the dataset.
"""

import csv
import math
from typing import List, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indexes for a paginated slice.

    Args:
        page: 1-based page number (>= 1).
        page_size: number of items per page (>= 1).

    Returns:
        A tuple (start, end) for slicing. Start is inclusive and end
        is exclusive.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with a dataset cache placeholder."""
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """
        Return the cached dataset, loading it from CSV on first call.

        The header row is skipped so the dataset contains only data rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a page of the dataset based on page and page_size.

        Validates inputs with assertions, computes indexes via index_range,
        and returns the appropriate list slice. If the start index is out
        of range, an empty list is returned.

        Args:
            page: 1-based page number (default 1).
            page_size: number of items per page (default 10).

        Returns:
            A list of rows for the requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data):
            return []
        return data[start:end]
