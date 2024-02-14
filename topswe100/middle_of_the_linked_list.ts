/*

link to problem: https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Input: head of a linked list
Output: the middle or second middle node of the list

we need the length of the linked list to find the middle, so we need to iterate through the entire list at least once

once we know the length of the linked list, we can either iterate backwards through the list to the halfway point or have made an array or other object to store nodes in

first solution: prioritize time

    i. initialize current node and an array to store nodes in

    ii. while current isn't null

        iii. push node into array

    iv. we have the length of the linked list and return the node at the Math.ceil (since we want the second middle node) index

*/

function middleNode(head: ListNode | null): ListNode | null {
    let slow: ListNode | null = head, fast: ListNode | null = head;

    while (fast !== null && fast.next !== null) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    return slow;
};

// let current: ListNode | null = head, memo: ListNode[] = [];

// while (current !== null) {
//     memo.push(current);
//     current = current.next;
// }

// const len = memo.length;

// return len % 2 === 0 ? memo[len / 2] : memo[Math.floor(len / 2)];