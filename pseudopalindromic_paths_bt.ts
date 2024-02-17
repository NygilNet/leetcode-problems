/*

link to problem: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

*/

function pseudoPalindromicPaths (root: TreeNode | null): number {

    let count = 0;
    let frequency = new Array(10).fill(0);

    function _dfs(root: TreeNode | null, frequency: number[]) {
        if (!root) return;
        
        // const newFrequency = [...frequency];
        // newFrequency[root.val]++;
        frequency[root.val]++;
        
        if (!root.left && !root.right) {
            if (frequency.filter(val => val % 2 === 1).length < 2) count++;
            return;
        }

        _dfs(root.left, frequency);
        _dfs(root.right, frequency);

        frequency[root.val]--;

    }

    _dfs(root, frequency);

    return count;

}
