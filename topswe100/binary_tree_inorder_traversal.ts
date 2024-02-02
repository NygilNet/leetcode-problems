/*

link to problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

*/



 class TreeNode {
     val: number
     left: TreeNode | null
     right: TreeNode | null
     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.left = (left===undefined ? null : left)
         this.right = (right===undefined ? null : right)
     }
 }
 

function inorderTraversal(root: TreeNode | null): number[] {

    return root ? [...inorderTraversal(root.left), root.val, ...inorderTraversal(root.right)] : [];

    // const res: number[] = [], stack: TreeNode[] = [];
    // let currentNode: TreeNode | null = root;

    // while (currentNode !== null || stack.length) {

    //     while (currentNode !== null) {
    //         stack.push(currentNode!);
    //         currentNode = currentNode!.left;
    //     }

    //     currentNode = stack.pop()!;
    //     res.push(currentNode!.val);
    //     currentNode = currentNode!.right;

    // }

    // return res;

}