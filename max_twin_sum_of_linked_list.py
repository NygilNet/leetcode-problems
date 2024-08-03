"""
link to leetcode: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        left,right = 0, len(lst) - 1
        max_sum = 0

        while left < right:
            l, r = lst[left], lst[right]
            max_sum = max(max_sum, l + r)
            left += 1
            right -= 1

        return max_sum