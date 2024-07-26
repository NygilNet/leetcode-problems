"""
link to leetcode: https://leetcode.com/problems/score-after-flipping-matrix/

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).
"""

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        

        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = -(grid[r][c] - 1)
                # grid[r] = list(map(lambda x: 1 if not x else 0, grid[r]))


        for c in range(COLS):
                zeroes = 0
                for r in range(ROWS):
                    if grid[r][c] == 0:
                        zeroes += 1

                if zeroes > ROWS - zeroes:
                    for r in range(ROWS):
                        grid[r][c] = -(grid[r][c] - 1)

        score = 0

        for r in range(ROWS):
            for c in range(COLS):
                score += grid[r][c] * 2**(COLS - c - 1)

        return score
