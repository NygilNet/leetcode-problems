"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

  
input: root of binary tree
output:


bfs
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def printLevelWiseBinaryTree(root: TreeNode) -> str:
        if not root:
            return ""
        
        res = ""
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            val, left, right = node

            res += f"{val}, "

            if left:
                queue.append((left, level + 1))
            if right:
                queue.append((right, level + 1))

        return res[0 : -2]