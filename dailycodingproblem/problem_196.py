"""
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def mostFrequentSumInSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sums = defaultdict(int)

        def _collectSums(node: TreeNode):
            # if not node.left and not node.right:
            #     sums[node.val] += 1
            #     return node.val
            
            left_sum = _collectSums(node.left) if node.left else 0
            right_sum = _collectSums(node.right) if node.right else 0

            total_sum = node.val + left_sum + right_sum
            sums[total_sum] += 1

            return total_sum
        
        _collectSums(root)

        key_of_max = None

        for sum in sums:
            if not key_of_max or sums[sum] > sums[key_of_max]:
                key_of_max = sum

        return sums[key_of_max]
        
tree = TreeNode(5, TreeNode(2), TreeNode(-5))
solution = Solution()

print(solution.mostFrequentSumInSubtree(tree))