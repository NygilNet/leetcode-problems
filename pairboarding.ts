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