/*

link to problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

we need to traverse the entire tree since any branch can have the max depth

a recursive method



*/

function maxDepth(root: TreeNode | null): number {
    // if (!root) return max;
    // return Math.max(maxDepth(root.left, max + 1), maxDepth(root.right, max + 1));

    let max = 0;
    const stack: [TreeNode | null, number][] = [[root, 1]];

    while (stack.length) {

        const [currentNode, currentDepth] = stack.pop()!;
        if (currentNode === null) continue;
        max = Math.max(max, currentDepth);

        stack.push([currentNode.left, currentDepth + 1]);
        stack.push([currentNode.right, currentDepth + 1]);

    }

    return max;

}