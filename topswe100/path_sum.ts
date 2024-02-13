/*

link to problem: https://leetcode.com/problems/path-sum/description/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

*/

function hasPathSum(root: TreeNode | null, targetSum: number, memo = new Map()): boolean {
    if (!root) return false;
    const current = targetSum - root.val;
    if ((!root.left && !root.right) && current === 0) return true;

    if (memo.has(root)) return memo.get(root);

    const result = hasPathSum(root.left, current, memo) || hasPathSum(root.right, current, memo);
    memo.set(root, result);
    return result;
};