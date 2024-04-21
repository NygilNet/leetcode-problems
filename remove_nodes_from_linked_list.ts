/*

link to leetcode: https://leetcode.com/problems/remove-nodes-from-linked-list/solutions/4821713/python-o-n-time-and-space-complexity/

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105

*/

function removeNodes(head: ListNode | null): ListNode | null {
    if (!head) {
        return null;
    }

    const sample: ListNode[] = [];
    let pointer: ListNode | null = head;

    while (pointer) {
        sample.push(pointer);
        pointer = pointer.next;
    }

    let last = sample.pop();
    let max = last.val;

    while (sample.length) {
        let current = sample.pop()!;
        if (current.val < max) {
            continue;
        } else {
            max = current.val;
            current.next = last;
            last = current;
        }
    }

    return last;
}

// function removeNodes(head: ListNode | null): ListNode | null {
//     const dummy = new ListNode();
//     let dummyPointer = dummy;
//     let conditionMet = false;
//     let current = head;

//     while (current) {
//         let fast = current.next;
//         while (fast) {
//             if (fast.val > current.val) {
//                 conditionMet = true;
//                 dummyPointer.next = fast;
//                 dummyPointer = dummyPointer.next;
//                 current = fast;
//                 break;
//             }
//             fast = fast.next;
//         }
//         current = current.next;
//     }

//     if (!conditionMet) {
//         dummy.next = head;
//     }

//     return dummy.next;
// }