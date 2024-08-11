"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode):
        if not root.left and not root.right:
            return bool(root.val)
        
        found_one_on_left = self.pruneTree(root.left)
        found_one_on_right = self.pruneTree(root.right)

        if not found_one_on_left:
            root.left = None
        if not found_one_on_right:
            root.right = None

        return found_one_on_left or found_one_on_right

        
        