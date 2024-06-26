"""
link to leetcode: https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = deque()
        stack.append((p, q))

        while stack:
            p_node, q_node = stack.pop()

            if not p_node and not q_node:
                continue
            if not p_node or not q_node or p_node.val != q_node.val:
                return False

            stack.append((p_node.left if p_node else None, q_node.left if q_node else None))
            stack.append((p_node.right if p_node else None, q_node.right if q_node else None))

        return True