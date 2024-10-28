"""
This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C.


Input: root of a directed graph (linked list)
Output: root of a reversed linked list



"""
class LinkedListNode:
    def __init__(self, val = "", next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverseDirectedGraph(self, head: LinkedListNode):
        current = head
        prev = None

        while current.next:
            save = current

            current.next = prev
            prev = current

            current = save.next

        return current