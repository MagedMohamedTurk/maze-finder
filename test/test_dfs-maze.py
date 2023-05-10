import sys
sys.path.append('/home/maged/repos/algos/dfs-maze/')

import dfs_maze

"""
Test dfs_maze module
TODO:
    1. Test maze that does not have any valid path
"""

maze1 = ["#######.##",
         "#S...##.##",
         "####......",
         "####.#####",
         "##...#####",
         "...#######",
         "##......##",
         "#######E##"]


def test_maze():
    param = maze1
    expected = 16
    assert dfs_maze.solve_maze(param) == expected


def test_find_s_e():
    param = maze1
    expected = (1, 1), (7, 7)
    assert dfs_maze.find_s_e(param) == expected


def test_is_valid():
    assert dfs_maze.is_valid(maze1, (1, 3))
    assert not dfs_maze.is_valid(maze1, (0, 0))


def test_explore_neighbors():
    param = [maze1, (1, 1)]
    expected = [(1, 2)]
    assert list(dfs_maze.explore_neighbors(param[0], param[1])) == expected
