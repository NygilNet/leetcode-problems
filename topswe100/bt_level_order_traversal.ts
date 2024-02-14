/*

link to problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

*/

function levelOrder(root: TreeNode | null): number[][] {
    if (!root) return [];
    const queue: [TreeNode, number][] = [[root, 0]], levelOrder: number[][] = [];

    while (queue.length) {
        const [{ val, left, right }, depth] = queue.shift()!;

        levelOrder[depth] ||= [];
        levelOrder[depth].push(val);

        if (left) queue.push([left, depth + 1]);
        if (right) queue.push([right, depth + 1]);
    }
    
    return levelOrder;
};

/*
public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        if (root == null) return [];
        Queue<(TreeNode, int)> queue = new Queue<(TreeNode, int)>();

        queue.Enqueue((root, 0))
    }
}

*/