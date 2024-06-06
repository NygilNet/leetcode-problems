"""
link to leetcode: https://leetcode.com/problems/minimum-falling-path-sum-ii/

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

"""

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # brute force
            # considers every valid option
                # not valid if same col
            # DFS/ backtracking
            # time complex: exponential O (n^n)
        # find cheapest path from previous row and accumulate the results
        # find solutions row by row
        # keep track of solutions in two rows since we only need to consider prev result

        N = len(grid)
        dp = grid[0].copy()

        for r in range(1, N):
            new_row = [float('inf')] * N

            min1 = min2 = float('inf')
            idx1 = -1
            for c in range(N):
                if dp[c] < min1:
                    min2 = min1
                    min1 = dp[c]
                    idx1 = c
                elif dp[c] < min2:
                    min2 = dp[c]
            
            for c in range(N):
                if c == idx1:
                    new_row[c] = min2 + grid[r][c]
                else:
                    new_row[c] = min1 + grid[r][c]

            dp = new_row

        return min(dp)