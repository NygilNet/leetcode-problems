"""
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:
   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPaths(self, root: TreeNode) -> list[int]:
        all_paths = []
        def _dfs(node: TreeNode | None, path = []):
            if not node:
                all_paths.append(path)
                return
            path.append(node.val)
            if node.left:
                _dfs(node.left, path.copy())
            if node.right:
                _dfs(node.right, path.copy())

        _dfs(root)
        return all_paths