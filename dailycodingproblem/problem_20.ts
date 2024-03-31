/*

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

*/

function findListIntersect(list1: ListNode, list2: ListNode): number {
    let intersect: number = -1;

    function _sortList(head: ListNode | null): void {
        let current: ListNode | null = head;
        let index: ListNode | null;

        if (!head) {
            return;
        }

        while (current) {
            index = current.next;
            while (index) {
                if (current.val > index.val) {
                    [current.val, index.val] = [index.val, current.val];
                }
                index = index.next;
            }
            current = current.next;
        }
    }

    function _determineCase(a: number, b: number): number {
        if (a === b) {
            return 0;
        } else if (a > b) {
            return 1;
        } else {
            return 2;
        }
    }

    function _findIntersect(listA: ListNode | null, listB: ListNode | null): void {
        let pointerA = listA, pointerB = listB;
        while (pointerA || pointerB) {
            const { val: valA, next: nextA } = pointerA ?? { val: Number.MAX_SAFE_INTEGER, next: null };
            const { val: valB, next: nextB } = pointerB ?? { val: Number.MAX_SAFE_INTEGER, next: null };
            if (intersect > -1 || (!nextA && !nextB)) {
                break;
            }
            const c = _determineCase(valA, valB);
            switch(c) {
                case 0:
                    intersect = valA;
                    break;
                case 1:
                    pointerB = nextB;
                    break;
                case 2:
                    pointerA = nextA;
                    break;
            }
        }
    }

    _sortList(list1);
    _sortList(list2);
    _findIntersect(list1, list2);

    return intersect;
}