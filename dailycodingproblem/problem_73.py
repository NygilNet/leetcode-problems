"""

Given the head of a singly linked list, reverse it in-place.

"""

def reverseLinkedList(root):
    if not root:
        return None
    
    prev, curr = None, root

    while curr.next:
        temp = curr.next

        curr.next = prev
        
        prev = curr
        curr = temp

    curr.next = prev
    return curr