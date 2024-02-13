/*

link to problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

*/

function minDepth(root: TreeNode | null): number {
    if (!root) return 0;
    let min: number;
    const queue: [TreeNode, number][] = [[root, 1]];
    while (queue.length) {
        const [{ val, left, right }, depth] = queue.shift()!;
        if (!left && !right) {
            min = depth; 
            break;
        } 
        if (left) queue.push([left, depth + 1]);
        if (right) queue.push([right, depth + 1]);
    }
    return min!; 
};

// if (!root) return 0;
// let min = Number.MAX_SAFE_INTEGER;
// const queue: [TreeNode, number][] = [[root, 1]];
// while (queue.length) {
//     const [{ val, left, right }, depth] = queue.shift()!;
//     if (!left && !right) {
//         min = Math.min(min, depth); 
//         break;
//     } 
//     if (left) queue.push([left, depth + 1]);
//     if (right) queue.push([right, depth + 1]);
// }
// return min;