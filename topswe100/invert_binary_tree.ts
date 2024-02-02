/*

link to problem: https://leetcode.com/problems/invert-binary-tree/description/

Given the root of a binary tree, invert the tree, and return its root.


starting w/ recursive solution at see if we can find a iterative solution

if root is null return

use deconstruction to swap left node and right node

call invertTree on left and right node

return root node after all other nodes have been switched

*/

function invertTree(root: TreeNode | null): TreeNode | null {

    if (root === null) return null;

    [root.left, root.right] = [root.right, root.left];

    invertTree(root.left);
    invertTree(root.right);

    return root;

};

