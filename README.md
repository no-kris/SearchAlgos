# Maze Pathfinding with Generic Search Algorithms

This program uses Depth-First Search (DFS), Breadth-First Search (BFS), and A* Search algorithms to find a path in a maze.

## Program Structure

The program consists of the following components:

1. **Maze Representation**: The maze is represented as a grid of cells, an instance of a maze object. Optional parameters for rows, columns, sparseness, start location, and goal location.

2. **Search Algorithms Implementation**:
   - Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
   - Breadth-First Search (BFS): Explores all neighbor nodes at the present depth before moving on to the nodes at the next depth level.
   - A* Search: Uses a heuristic function to estimate the cost from the start node to the goal node.

3. **Node**: A node represents attributes for state, parent, cost, and heuristic.

4. **Stack**: A LIFO data structure used for depth-first search.

5. **Queue**: A FIFO data structure used for breadth-first search.

6. **Priority Queue**: A type of queue where the elements are stored based on priority. In this case, it is the smallest priority for A* search.

## How to Use

1. **Input**: Provide the maze layout as input to the program, optionally pass in the number of rows and columns, the sparseness of the maze, start location and goal location.

2. **Run the Program**: Execute the program to apply the search algorithms on the maze and find a path from the starting point to the goal point.

3. **Output**: The program outputs the path found by each algorithm to the command line.

## Dependencies

- Python 3.x
- Any necessary libraries for handling data structures.
