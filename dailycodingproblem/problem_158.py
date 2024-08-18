"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""

class Solution:
    def countPossiblePaths(matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        NEIGHBORS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        global paths
        paths = 0

        def _inbounds(r: int, c: int) -> bool:
            return (0 <= r < ROWS) and (0 <= c < COLS)

        def _dfs(r: int, c: int, seen: set[tuple[int,int]]):
            if r == ROWS - 1 and c == COLS - 1:
                paths += 1
                return
            
            for dr, dc in NEIGHBORS:
                new_row, new_col = r + dr, c + dc
                if _inbounds(new_row, new_col) and matrix[new_row][new_col] == 0 and (new_row, new_col) not in seen:
                    new_seen = seen.copy()
                    new_seen.add((new_row, new_col))
                    _dfs(new_row, new_col, new_seen)

        _dfs(0, 0, set([(0, 0)]))
        return paths