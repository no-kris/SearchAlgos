from typing import Generic
from collections import deque
from node import T


class Queue(Generic[T]):
    """Create a basic FIFO queue data structure."""
    def __init__(self):
        self.container = deque()

    @property
    def empty(self):
        return not self.container

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.popleft()

    def __repr__(self):
        return repr(self.container)
