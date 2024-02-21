/*

link to problem: https://leetcode.com/problems/linked-list-cycle/description/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


iterate through the linked list

 find some way to mark that we have visited a node

 if we have visited a node, return true

 if we make it to the end of the list w/o returning true, return false

*/

class ListNode {
         val: number
         next: ListNode | null
         constructor(val?: number, next?: ListNode | null) {
             this.val = (val===undefined ? 0 : val)
             this.next = (next===undefined ? null : next)
         }
     }

function hasCycle(head: ListNode | null): boolean  {
    let slow: ListNode | null = head, fast: ListNode | null | undefined = head;
    while (fast) {
        slow = slow!.next;
        fast = fast.next?.next;
        if (slow === fast) return true;
    }
    return false;
}

// O(n) space complexity
// function hasCycle(head: ListNode | null, set: Set<ListNode> = new Set()): boolean {
//     if (!head) return false;
//     if (set.has(head)) return true;
//     set.add(head);
//     hasCycle(head.next, set);
// }