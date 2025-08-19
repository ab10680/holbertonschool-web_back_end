#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Return a deletion-resilient page and navigation indexes.

        Args:
            index: starting index to fetch from (defaults to 0 if None).
            page_size: number of items to return.

        Returns:
            dict with:
              - index: the current start index of the return page
              - next_index: index to query next (or None at the end)
              - page_size: actual number of items returned
              - data: the page data (list of rows)
        """
        data_map = self.indexed_dataset()

        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        assert index < len(data_map)

        items: List[List[str]] = []
        current = index
        max_key = max(data_map.keys()) if data_map else -1

        while len(items) < page_size and current <= max_key:
            if current in data_map:
                items.append(data_map[current])
            current += 1

        next_index: Optional[int]
        next_index = current if current <= max_key else None

        return {
            "index": index,
            "data": items,
            "page_size": len(items),
            "next_index": next_index,
        }
