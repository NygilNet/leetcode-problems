/*

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

*/


function countUnivalSubtrees(root: TreeNode): number {
    let count: number = 0;

    const stack: TreeNode[] = [root];

    while (stack.length) {
        const { val, left, right } = stack.pop()!;
        if ((left === null && right === null) || (left?.val === right?.val)) {
            count++;
        }
        if (left) {
            stack.push(left);
        }
        if (right) {
            stack.push(right);
        }
    }

    return count;
}