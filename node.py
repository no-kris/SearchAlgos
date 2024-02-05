from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    """
    Node class, used to represent a generic node that consists of
    a state, parent, cost, and heuristic.
    """

    def __init__(self, state, parent=None, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
