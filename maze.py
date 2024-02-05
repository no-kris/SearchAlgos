import math
from enum import Enum
from typing import NamedTuple
import random

from generic_search import dfs, node_to_path, bfs, astar


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "█"
    START = "🏁"
    GOAL = "🎯"
    PATH = "•"


class MazeLocation(NamedTuple):
    row: int
    column: int


def euclidean_distance(goal):
    """
    Calculate the Euclidean distance between two points.
    :param goal: The goal state.
    :return: The Euclidean distance from the goal state.
    """
    def distance(coord):
        x_dist = coord.column - goal.column
        y_dist = coord.row - goal.row
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

    return distance


def manhattan_distance(goal):
    """
    Calculate the Manhattan distance between two points.
    :param goal: The goal state.
    :return: The Manhattan distance from the goal state.
    """
    def distance(coord):
        x_dist = abs(coord.column - goal.column)
        y_dist = abs(coord.row - goal.row)
        return x_dist + y_dist

    return distance


class Maze:
    """
    Maze class, used for creating a maze. Consists of rows, columns,
    sparseness, start location, and goal location.
    """
    def __init__(self, rows=10, columns=10, sparseness=0.2, start=MazeLocation(0, 0),
                 goal=MazeLocation(9, 9)):
        self.rows = rows
        self.columns = columns
        self.start = start
        self.goal = goal
        self.grid = [[Cell.EMPTY for c in range(columns)]
                     for r in range(rows)]
        self.randomly_fill(rows, columns, sparseness)
        self.grid[start.row][start.column] = Cell.START
        self.grid[goal.row][goal.column] = Cell.GOAL

    def randomly_fill(self, rows, columns, sparseness):
        """
        Randomly fill the maze with BLOCKED figures representing where
        the state can not pass.
        """
        for row in range(rows):
            for col in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self.grid[row][col] = Cell.BLOCKED

    def successors(self, current):
        """
        Generate a list of successors of the current maze location. Checks if node
        can move up, down, left, or right.
        :param current: Current maze location.
        :return: A list of successors of the current maze location.
        """
        locations = []
        # move to the right
        if current.row + 1 < self.rows and \
                self.grid[current.row + 1][current.column] != Cell.BLOCKED:
            locations.append(MazeLocation(current.row + 1, current.column))
        # move to the left
        if current.row - 1 >= 0 and \
                self.grid[current.row - 1][current.column] != Cell.BLOCKED:
            locations.append(MazeLocation(current.row - 1, current.column))
        # move up
        if current.column + 1 < self.columns and \
                self.grid[current.row][current.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(current.row, current.column + 1))
        # move down
        if current.column - 1 >= 0 and \
                self.grid[current.row][current.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(current.row, current.column - 1))
        return locations

    def goal_test(self, location):
        """
        :return: Whether the current location is the goal state.
        """
        return location == self.goal

    def mark(self, path):
        """Mark the current path from the start state to the goal state."""
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        """Clear the current path from the start state to the goal state."""
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self):
        """Print the maze."""
        output = ""
        for row in self.grid:
            output += "".join([c.value for c in row]) + "\n"
        return output


if __name__ == "__main__":
    print("Current maze")
    maze = Maze(10, 50, .2, goal=MazeLocation(5, 47))
    print(maze)
    solution1 = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print("No solution")
    else:
        print("Solution found using depth-first search")
        path1 = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)
    print()
    solution2 = bfs(maze.start, maze.goal_test, maze.successors)
    if solution2 is None:
        print("No solution")
    else:
        print("Solution found using breadth-first search")
        path2 = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)
    print()
    solution3 = astar(maze.start, maze.goal_test, maze.successors, manhattan_distance(maze.goal))
    if solution3 is None:
        print("No solution")
    else:
        print("Solution found using astar")
        path3 = node_to_path(solution3)
        maze.mark(path3)
        print(maze)
