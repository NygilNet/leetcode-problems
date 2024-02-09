/*

link to leetcode: https://leetcode.com/problems/design-linked-list/description/

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

*/

// hashmap can help us keep track of indices in linked list
// need a head to start
// use two dummy nodes for head and tail to address edge cases (empty list)

class LinkedListNode {
    val: number
    next: LinkedListNode | null
    prev: LinkedListNode | null

    constructor(val: number) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class MyLinkedList {
    head: LinkedListNode
    tail: LinkedListNode
    length: number

    constructor() {
        this.head = new LinkedListNode(-1);
        this.tail = new LinkedListNode(-1);
        this.length = 0;

        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    get(index: number): number {
        if (this.length - 1 < index) return -1;
        
        let current = this.head.next;
        let i = 0;

        while (current) {
            if (i === index) return current.val;
            current = current.next;
            i++;
        }

        return -1;
    }

    addAtHead(val: number): void {
        const node = new LinkedListNode(val);
        const nxt = this.head.next;

        this.head.next = node;
        node.prev = this.head;

        node.next = nxt;
        nxt!.prev = node;

        this.length++;
    }

    addAtTail(val: number): void {
        const node = new LinkedListNode(val);
        const prv = this.tail.prev;

        prv!.next = node;
        node.prev = prv;
        
        node.next = this.tail;
        this.tail.prev = node;

        this.length++;
    }

    addAtIndex(index: number, val: number): void {
        // if (index < 0 || index > this.length) return;
    
        const node = new LinkedListNode(val);
        
        let current = this.head;
        for (let i = 0; i < index; i++) {
            current = current.next!;
        }
    
        const nxt = current.next;
        const prv = current;
    
        prv.next = node;
        node.prev = prv;
    
        node.next = nxt;
        nxt!.prev = node;
    
        this.length++;
    }

    deleteAtIndex(index: number): void {
        if (index < 0 || index > this.length) return;
        
        let current = this.head;
        for (let i = 0; i < index; i++) {
            current = current.next!;
        }
        
        let nxt = current.next;
        let prv = current.prev;

        nxt!.prev = prv;
        prv!.next = nxt;

        this.length--;
    }
}