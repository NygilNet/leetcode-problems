/*

Write an algorithm that, given a Binary Search Tree, will find the second largest node in the tree. Assume you already have a bst Node class with an insert method.


       _10_
      _/    \_          
     5        15
    / \       / \
   3   8     12  20
  /     \         \
 2       4        30

Output: 20


   10
    /  
   5
  / \
 3   7

Output: 7


input: root node of bst
output: node w/ second largest val

Node:
    constructor(val, left, right) {

    }

    insert() {

    }


from the root,
move right if you are able
if you can't move right, but are not at a leaf node, move left
continue this until you reach the leaf node and the farthest right end of the tree
return the parent of that leaf node

*/

function secondLargestNode(root, prevVal= null) {
    if (!root && prevVal === null) {
        return -1;
    }

    const { val, left, right } = root;
    if (!left && !right) {
        return prevVal;
    }
    if (right) {
        return secondLargestNode(right, val);
    } else if (!right && left) {
        return secondLargestNode(left, val);
    }
}




/*Reverse a Linked List
You are given the pointer to the head node of a linked list. Your goal is to reverse this list. A linked list is implemented using just a Node class, which you will be given. The Node class is defined as:

function Node(data, next = null) {
  this.data = data;
  this.next = next;
}
Your function should take in just the head node, reverse the list, and return the new head node (which would be the old tail node). Remember that an empty linked list is still a valid linked list. If null is passed into your function, your function should return null.

Note that this class does not have a previous attribute. Make sure your partner is using a Node object similar to the one above!

Constraints:

Your function must run in O(n) time and O(1) space */

/*

input: head of linked list or null
output: head of reserved list or null


iterative solution

   1 -> 2 -> 3

   3 -> 2 -> 1

   traverse through the original list to create a stack
   traverse through the stack to build the reserved list


recursive solution

    1 -> 2 -> 3

    3 2 1

*/

class TNode {
    data: number
    next: TNode | null

    constructor(data?: number, next?: TNode) {
        this.data = (data === undefined ? 0 : data);
        this.next = (next === undefined ? null : next);
    }
}

function reverseList(head: TNode | null): TNode | null {
    let current: TNode | null = head;
    const stack: number[] = [];

    while (current) {
        const { data, next } = current;
        stack.push(data);
        current = next;
    }

    const dummy: TNode = new TNode();
    let pointer = dummy;

    while (stack.length) {
        const val = stack.pop();
        const newNode = new TNode(val);

        pointer.next = newNode;
        pointer = newNode;
    }

    return dummy.next;
}



/*

1 -> 2 -> 3 
            
        <-|

A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named head that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.


input: head of linked list
output: boolean (whether or not there is a cycle in the list)


traverse through the list 
add a new property "visited" to each node set to true
if we encounter a node with the visited key before pointer is null, there is a cycle in the list


traverse through the list 
we have a slow pointer and a fast pointer (with goes two steps in the list instead of one)
if at any point fast == slow, there is a cycle in the list
if fast because null, there is no cycle

*/

function cycleDetective(head: TNode): boolean {
    let slow: TNode | null = head;
    let fast: TNode | null = head;
    

    while (slow && fast) {
        slow = slow.next;
        fast = fast?.next.next || null;

        if (slow === fast) {
            return true;
        }
    }

    return false;
}




