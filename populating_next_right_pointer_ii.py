"""
link to problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

CAN NOT:
    queue/stack (space O(width of the tree))

"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return None
    
    current = root
    dummy = Node(-101)
    head = root

    while head:
        current = head
        prev = dummy

        while current:
            if current.left:
                prev.next = current.left
                prev = prev.next
            if current.right:
                prev.next = current.right
                prev = prev.next
            current = current.next
        
        head = dummy.next
        dummy.next = None

    return root