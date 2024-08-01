"""
link to leetcode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def flatten(self, root: TreeNode | None):
        def _preorder(r: TreeNode | None) -> list[TreeNode]:
            if not r:
                return []
            return [r] + _preorder(r.left) + _preorder(r.right)
        
        stack = deque(_preorder(root))
        while stack:
            curr = stack.popleft()
            n = stack[0] if stack else None

            curr.left = None
            curr.right = n

        return root
            
