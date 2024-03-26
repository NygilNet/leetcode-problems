/*

link to leetcode: https://leetcode.com/problems/odd-even-linked-list/description/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

  Definition for singly-linked list.
  class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }


CAN NOT:
sort (O n log n time)
additional loops in a loop (O n^2 time)
array/map (O n space)



*/

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function oddEvenList(head: ListNode | null): ListNode | null {
    let current: ListNode | null = head;
    let evenHead: ListNode | null = null, even: ListNode | null;
    while (current?.next) {
        if (evenHead === null) {
            evenHead = current.next;
            even = evenHead;
        } 
        [current.next, even!.next] = [even!.next, null];
        current = current.next;
    }
    current.next = evenHead;
    return head;
}