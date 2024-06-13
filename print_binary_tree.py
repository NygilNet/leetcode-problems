"""
link to leetcode: https://leetcode.com/problems/print-binary-tree/description/

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

input: binary tree
output: matrix of strings

find the width and the depth of the binary tree
    this helps us figure out how big of a matrix to create
    if we find depth, we know how many rows we need
    we can derive the # of cols from the depth

we can prebuild the matrix using the info above
we can figure out where to place nodes by calucating cols
fill out matrix values layer by layer using BFS

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def printTree(self, root: TreeNode) -> list[list[str]]:
        def _get_depth(node: TreeNode, level: int = 0) -> int:
            if not node:
                return level
            return max(_get_depth(node.left, level + 1), _get_depth(node.right, level + 1))
        

        ROWS = _get_depth(root)
        COLS = 2 ** (ROWS) - 1

        res = [ [""] * COLS for _ in range(ROWS)]
        queue = deque()
        queue.append((root, 0, (COLS - 1) // 2))

        while queue:
            node, row, col = queue.popleft()

            res[row][col] = str(node.val)

            if node.left:
                queue.append((node.left, row + 1, (col - 2 ** (ROWS - row - 2))))
            if node.right:
                queue.append((node.right, row + 1, (col + 2 ** (ROWS - row - 2))))

        return res
    