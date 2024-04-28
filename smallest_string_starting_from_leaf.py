"""

link to leetcode: https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def _findSmallest(node: TreeNode):
        if not node.left and not node.right:
            return ALPHABET[node.val]

        smallest = ""
        left = _findSmallest(node.left) if node.left else None
        right = _findSmallest(node.right) if node.right else None

        if left and right:
            if left < right:
                smallest = left
            elif left > right:
                smallest = right
            else:
                smallest = left
        else:
            if left:
                smallest = left
            else:
                smallest = right

        return smallest + ALPHABET[node.val]

    return _findSmallest(root)