"""

You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determines its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order.
Sample Input:

[
  [1,0,0,1,0],
  [1,0,1,0,0],
  [0,0,1,0,1],
  [1,0,1,0,1],
  [1,0,1,1,0]
]

Sample Output:

=> [1,2,2,2,5]


Input: matrix (of 1s and 0s)
Output: array of ints (how long each river in the matrix is)


dfs method:
i. define a helper that finds all the neighbors of a 1, converts them to 0, and returns the number of 1s encountered
ii. iterate through the matrix until we find a 1
iii. call the helper function and push the result into a res array
iv. continue until end of matrix
v. return the res array 


"""

from collections import deque
class Solution:
    def lengthOfRivers(matrix: list[list[int]]) -> list[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        NEIGHBORS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def _inbounds(r: int, c: int) -> bool:
            return (0 <= r < ROWS) and (0 <= c < COLS)

        def _dfs(row: int, col: int):
            count = 0
            stack = deque()
            stack.append((row, col))
            matrix[row][col] = 0

            while stack:
                count += 1
                r,c = stack.pop()

                for dr, dc in NEIGHBORS:
                    new_row, new_col = r + dr, c + dc
                    if (_inbounds(new_row, new_col) and matrix[new_row][new_col] == 1):
                        matrix[new_row][new_col] = 0
                        stack.append((new_row, new_col))

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    res.append(_dfs(r, c))

        return res
    

r = Solution.lengthOfRivers([
  [1,0,0,1,0],
  [1,0,1,0,0],
  [0,0,1,0,1],
  [1,0,1,0,1],
  [1,0,1,1,0]
])

print(r)