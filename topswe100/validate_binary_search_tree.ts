/*

link to problem: https://leetcode.com/problems/validate-binary-search-tree/description/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.

The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.

create a stack

while there are nodes in the stack

    return false if node.left is greater than node.val or node.right is less than node.val

if we make it to the end without returning false return true

*/



function isValidBST(root: TreeNode | null): boolean {
    if (root === null) return true;
    const stack: [TreeNode, number, number][] = [[root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]];

    while (stack.length) {
        const [{ val, left, right }, min, max ] = stack.pop()!;

        if (val <= min || val >= max) return false;

        if (left !== null) stack.push([left, min, val]);
        if (right !== null) stack.push([right, val, max]);
    }

    return true;
}