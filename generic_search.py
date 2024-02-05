from stack import Stack
from queue import Queue
from priority_queue import PriorityQueue
from node import Node


def dfs(initial, goal_test, successors):
    """
    Find the goal state using depth-first search.
    :param initial: Initial state.
    :param goal_test: Callable for checking if the goal is met.
    :param successors: Callable for generating a list of successor states.
    :return: A node representing the goal state, else none if goal was not found.
    """
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def bfs(initial, goal_test, successors):
    """
    Find the goal state using breadth-first search.
    :param initial: Initial state.
    :param goal_test: Callable for checking if the goal is met.
    :param successors: Callable for generating a list of successors states.
    :return: A node representing the goal state, else None if goal was not found.
    """
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def astar(initial, goal_test, successors, heuristic):
    """
    Find the goal state using astar, with heuristic and path-cost value.
    :param initial: Initial state.
    :param goal_test: Callable for checking if the goal is met.
    :param successors: Callable for generating a list of successor states.
    :param heuristic: Callable for calculating the heuristic to the goal state from the current state.
    :return: A node representing the goal state, else None if goal is not found.
    """
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


def node_to_path(node):
    """
    Generate a list of states that lead from the initial state to the goal state.
    :param node: A generic node.
    :return: A list of states.
    """
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
