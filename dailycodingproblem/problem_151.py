"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
"""

from collections import deque
class Solution:
    def replaceColorOnScreen(matrix: list[list[str]], location: tuple[str, str], color: str):
        _x, _y = location
        ROWS, COLS = len(matrix), len(matrix[0])
        TARGET = matrix[_x][_y]
        NEIGHBORS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def _inbounds(r: int, c: int) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS

        queue = deque()
        queue.append(location)

        while queue:
            r, c = queue.popleft()

            matrix[r][c] = color

            for dr, dc in NEIGHBORS:
                new_row, new_col = r + dr, c + dc

                if _inbounds(new_row, new_col) and matrix[new_row][new_col] == TARGET:
                    queue.append((new_row, new_col))