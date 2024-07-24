"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

"""
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def minPathSum(self, root:TreeNode|None) -> int:
        if not root:
            return float('inf')
        if not root.left and not root.right:
            return root.val
        
        left_sum = self.minPathSum(root.left)
        right_sum = self.minPathSum(root.right)

        return root.val + min(left_sum, right_sum)