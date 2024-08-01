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

# from collections import deque
class Solution:
    def flatten(self, root: TreeNode | None):
        def _dfs(node):
            if not node:
                return None
            
            left_tail = _dfs(node.left)
            right_tail = _dfs(node.right)

            if node.left:
                tmp = node.right
                node.right = node.left
                left_tail.right = tmp
                node.left = None

            if right_tail:
                return right_tail
            elif left_tail:
                return left_tail
            else:
                return node
        
        _dfs(root)

        # def _preorder(r: TreeNode | None) -> list[TreeNode]:
        #     if not r:
        #         return []
        #     return [r] + _preorder(r.left) + _preorder(r.right)
        
        # queue = deque(_preorder(root))
        # while queue:
        #     curr = queue.popleft()
        #     nxt = queue[0] if queue else None

        #     curr.left = None
        #     curr.right = nxt

        # return
            
