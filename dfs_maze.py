"""
This is a module that represent a demo for depth First Search algorithm.
The algorithm is used for finding the shortest path in a maze between S and E
Similar to "Dungeon Problem".
Module is also built using TDD (Test Driven Development) technique using Pytest module.
"""

# parent is a dictionary that collects the shortest path nodes
parent = {}


def solve_maze(maze):
    """
    Solve the maze problem where "S" is the source and "E" is the end point and
    "." represents the legal path
    The problem is to count the shortest path distance between "S" and "E"

    :param maze: The maze in grid form to be solved
    :type maze: List(str)
    :return: length of the shortest path or -1 if not found
    :rtype: int

    """
    s, e = find_s_e(maze)
    parent[s] = None
    dfs(maze, s, e)
    return len(parent)


def dfs(maze, s, e):
    """
    Carries out depth first search for the maze recursively
    Modifies the parent dictionary

    :param maze: The maze in grid form to be solved
    :type maze: List(str)
    :param s: Source node in Cartesian form (number of row, number of column)
    :type s: Tuple
    :param e: End point in Cartesian form (number of row, number of column)
    :return: Tuple
    :rtype: None
    """
    for neighbor in explore_neighbors(maze, s):
        if neighbor not in parent:
            parent[neighbor] = s
            if neighbor == e:
                return
            return dfs(maze, neighbor, e)
    return -1


def find_s_e(maze):
    """
    Parse the maze list to find the source node "S" and "E" node

    :param maze: The maze in grid form to be solved
    :type maze: List(str)
    :return: Source and End node
    :rtype: pack of two Tuples
    """
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == 'S':
                s = (i, j)
            if char == 'E':
                e = (i, j)
    return s, e


def explore_neighbors(maze, node):
    """
    find all valid neighbors of a node

    :param maze: The maze in grid form to be solved
    :type maze: List(str)
    :param node: node to be explored
    :type node: Tuple
    :return: All valid neighbor nodes
    :rtype: generator of tuples
    """
    x, y = node
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(dx)):
        next_x = x + dx[i]
        next_y = y + dy[i]
        next_node = (next_x, next_y)
        if is_valid(maze, next_node):
            yield next_node


def is_valid(maze, node):
    """
    Test if node is valid.
    Node is valid if it is not out of maze boundaries and the node value is "."

    :param maze: The maze in grid form to be solved
    :type maze: List(str)
    :param node: node to be explored
    :type node: Tuple
    :return: Boolean
    """

    x, y = node
    return len(maze) > x >= 0 and len(maze[0]) > y >= 0 and maze[x][y] == '.'
