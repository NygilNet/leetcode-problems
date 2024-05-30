"""

This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

INPUT: root of binary tree
OUTPUT: value? of one of the deepest nodes

bfs

tuple to store the depth of the deepest node and value

"""

from collections import deque
def deepestNode(root) -> str:
    if not root:
        return ""
    
    deepest_node = (0, "")
    queue = deque()
    queue.append((root, 1))

    while queue:
        node, level = queue.popleft()
        deepest, _ = deepest_node

        if level >= deepest:
            deepest_node = (level, node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return deepest_node[1]