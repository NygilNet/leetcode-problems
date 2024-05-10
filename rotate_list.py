"""
link to leetcode: https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

Input: head of a linked list, int
Output: rotated linked list

METHOD 1: Two-pointer
    i. initialize a fast pointer that is k places ahead of a slow pointer
        ii. if fast pointer reaches the end of the list before k, start at the beginning of the list again
    iii. while fast pointer
        iv. advance slow and fast pointer one place
        v. if not fast.next
            vi. set slow.next to null and fast.next to the head of the linked list
        

"""
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: list) -> Optional[ListNode]:
    if not head:
        return None
    
    curr = head
    size = 1

    while curr.next is not None:
        curr = curr.next
        size += 1
    
    curr.next = head

    i = size - (k % size)

    while i > 1:
        head = head.next
        i -= 1

    curr = head.next
    head.next = None
    return curr

"""
  if not head:
        return None
    if not head.next:
        return head
    
    fast = head

    while k < 0:
        if not fast.next:
            fast = head
        else:
            fast = fast.next

        k -= 1

    if fast == head:
        return head
    
    prev = None
    slow = head

    while fast:
        if not fast.next:
            prev.next = None
            fast.next = head
            break
        else:
            prev = slow
            slow = slow.next
            fast = fast.next

    return slow

"""