"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.



"""
class SingleLinkedListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def swapEveryNodeInLinkedList(self, head: SingleLinkedListNode) -> SingleLinkedListNode:
        dummy = SingleLinkedListNode()
        dummy.next = head
        tail = None
        node = head

        while node.next:
            tmp = node.next.next
            current_node, next_node = node, node.next
            if tail:
                tail.next = next_node
            current_node.next = None
            next_node.next = current_node
            tail = current_node
            
            if dummy.next == head:
                dummy.next = next_node

            node = tmp

        return dummy.next