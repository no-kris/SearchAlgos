from heapq import heappush, heappop
from typing import Generic
from node import T


class PriorityQueue(Generic[T]):
    """Create a priority queue where items are sorted in ascending order
       with the smallest item at the front."""

    def __init__(self):
        self.container = []

    @property
    def empty(self):
        return not self.container

    def push(self, item):
        heappush(self.container, item)

    def pop(self):
        return heappop(self.container)

    def __repr__(self):
        return repr(self.container)
