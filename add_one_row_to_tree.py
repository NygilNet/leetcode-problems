"""
link to leetcode: https://leetcode.com/problems/add-one-row-to-tree/description/

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Input: 



we need to track the depth of the tree -> bfs


when we get to depth - 1, we want to create two new nodes with value of val
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        # we want to add our edge case before line 22, where if the depth is equal to 1, we create a new TreeNode is value val, left of root, and right of None and return that
        if depth == 1:
            new_tree = TreeNode(val, root, None)
            return new_tree
        
        queue = deque([(root, 1)])

        while queue:
            node, layer = queue.popleft()

            if layer == depth - 1:
                new_left = TreeNode(val, node.left, None)
                new_right = TreeNode(val, None, node.right)
                # reassign node left and right to the new nodes, and since we don't need to traverse deeper into the tree, we can just move on the the next item in the queue
                node.left = new_left
                node.right = new_right
            else:
                if node.left:
                    queue.append((node.left, layer + 1))
                if node.right:
                    queue.append((node.right, layer + 1))

        return root