"""
This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
"""
class RandomLinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        self.rand = None

class Solution:
    def deepCloneRandomLinkedList(self, head: RandomLinkedListNode) -> RandomLinkedListNode:
        nodes = {}
        to_be_set = {}
        pointer = head
        dummy = RandomLinkedListNode(0)
        prev = dummy

        while pointer:
            val, next, rand = pointer

            current_node = RandomLinkedListNode(val)

            if val in to_be_set:
                to_be_set[val].rand = current_node
            elif rand.val in nodes:
                current_node.rand = nodes[rand.val]
            else:
                to_be_set[val] = current_node

            prev.next = current_node
            prev = prev.next
            pointer = next

        return dummy.next

