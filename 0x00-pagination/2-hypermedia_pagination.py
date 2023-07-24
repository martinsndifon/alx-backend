#!/usr/bin/env python3
"""ALX SE"""
import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size 2 containing a start and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


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
        """Gets and returns the paginated lines from the file"""
        assert isinstance(page, int) and page > 0, "Handled by main fn"
        assert isinstance(page_size, int) and page_size > 0, "Handled by main"

        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """Returns more information in a dict from get_page call"""
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        page_size = len(data)
        next_page = page + 1 if page + 1 <= total_pages else None

        prev_page = page - 1
        if page == 1:
            prev_page = None

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
