/*

link to problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

*/



class DoublyLinkedListNode {
    val: number
    prev: DoublyLinkedListNode | null
    next: DoublyLinkedListNode | null
    child: DoublyLinkedListNode | null
    constructor(val?: number, prev? : DoublyLinkedListNode, next? : DoublyLinkedListNode, child? : DoublyLinkedListNode) {
        this.val = (val===undefined ? 0 : val);
        this.prev = (prev===undefined ? null : prev);
        this.next = (next===undefined ? null : next);
        this.child = (child===undefined ? null : child);
    }
}

// function flatten(head: DoublyLinkedListNode | null): DoublyLinkedListNode | null {
//     if (!head) {
//         return null;
//     }

//     function _flattenDfs(prev: DoublyLinkedListNode, curr: DoublyLinkedListNode | null): DoublyLinkedListNode {
//         if (!curr) {
//             return prev;
//         }

//         curr.prev = prev;
//         prev.next = curr;
//         const nxt = curr.next

//         const tail = curr.child ? _flattenDfs(curr, curr.child) : curr;
//         curr.child = null;
//         return _flattenDfs(tail, nxt);
//     }

//     const dummy = new DoublyLinkedListNode(0, undefined, head ? head : undefined, undefined);
//     _flattenDfs(dummy, head);

//     return dummy.next;
// }

function flatten(head: DoublyLinkedListNode | null): DoublyLinkedListNode | null {
    let current: DoublyLinkedListNode | null = head;
    while (current) {
        const { next, child } = current;
        if (child) {
            const flattenHead = flatten(child)!;
            flattenHead.prev = current;
            current.next = flattenHead;
            current.child = null;
            while (current.next) {
                current = current.next;
            }
            current.next = next;
            if (next) {
                current = next;
            }
        }
        current = next;
    }
    return head;
}