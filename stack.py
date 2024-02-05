from typing import Generic
from node import T


class Stack(Generic[T]):
    """Create a basic LIFO Stack data structure."""

    def __init__(self):
        self.container = []

    @property
    def empty(self):
        return not self.container

    def push(self, item):
        self.container.append(item)

    def pop(self) -> T:
        return self.container.pop()

    def __repr__(self):
        return repr(self.container)
