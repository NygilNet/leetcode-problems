/*

link to leetcode: https://leetcode.com/problems/longest-univalue-path/description/

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Input: root of TreeNode
Output: number of edges of longest path


dfs to traverse entire tree

    base case: node is null, return 0
    check if parent has the same value of child(ren)
    return max(left, right) + 1
    if child does not equal the current node, do not take its return value


*/

function longestUnivaluePath(root: TreeNode | null): number {
    let longest = 0;

    function _dfs(node: TreeNode | null): number {
        if (!node) {
            return 0;
        }

        const { val, left, right } = node;

        const l = _dfs(left);
        const r = _dfs(right);

        let leftPath: number = left?.val === val ? l : 0;
        let rightPath: number = right?.val === val ? r : 0;

        const pathLen = leftPath + rightPath + 1;
        longest = Math.max(longest, pathLen);

        return pathLen;
    }

    _dfs(root);
    return longest;
}