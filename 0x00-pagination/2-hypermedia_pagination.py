#!/usr/bin/env python3
""" This module implements real pagination """
import csv
import math
from typing import List, Tuple


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
        """Returns a query of items in one page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        try:
            idx_start = index_range(page, page_size)[0]
            idx_end = index_range(page, page_size)[1]
            return dataset[idx_start:idx_end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictoinary containing page details"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        hyper = {}
        pg_size = len(self.get_page(page, page_size))
        data = self.get_page(page, page_size)
        next_page = page + 1 if self.get_page(page + 1, page_size) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = len(self.dataset()) / page_size

        hyper["page_size"] = pg_size
        hyper["page"] = page
        hyper["data"] = data
        hyper["next_page"] = next_page
        hyper["prev_page"] = prev_page
        hyper["total_pages"] = math.ceil(total_pages)

        return hyper
