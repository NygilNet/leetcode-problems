"""

link to leetcode: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

"""
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    adj_list = defaultdict(list)

    def _buildAdjacencyList(node, parent=None):
        if not node:
            return   
        
        if parent:
            adj_list[node.val].append(parent.val)
            adj_list[parent.val].append(node.val)
        
        _buildAdjacencyList(node.left, node)
        _buildAdjacencyList(node.right, node)

    _buildAdjacencyList(root)

    queue = deque([(start, 0)])
    visited = set()
    max_time = 0

    while queue:
        node, minutes = queue.popleft()
        max_time = minutes

        visited.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, minutes + 1))

    return max_time
