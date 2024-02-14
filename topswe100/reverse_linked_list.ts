/*

link to problem: https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

*/

class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function reverseList(head: ListNode | null/*, prev: ListNode | null = null*/): ListNode | null {
    // if (!head) return null;
    // const { val, next } = head;
    
    // const tempPrev = head;
    // head.next = prev;
    
    // if (!next) return head;
    // return reverseList(next, tempPrev);

    let prev: ListNode | null = null, current: ListNode | null = head;

    while (current !== null) {
        const nextTemp: ListNode | null = current.next;
        current.next = prev;
        [prev, current] = [current, nextTemp];
    }

    return prev;
}