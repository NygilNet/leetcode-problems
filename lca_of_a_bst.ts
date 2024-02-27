/*

link to leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: bst, two nodes at will be in the tree
Output: number, the lowest node that can "acess" p and q

first idea:
    breath first search
        descend through the bst until we find either p or q
        when we find p or q, check the next level down for the other node
        if we find the other node in the next level, return the first node we found
        if we don't find the other node, return the node from the level up

second idea:

   [6, 2, 0]
   [6, 2, 4, 5]

    create stack for each route:
        descend through the bst using backtracking or dfs
        generate a stack of all the nodes through the tree
        if the two stack are different lengths, we will ignore the x number of nodes in the larger stack
        when the two stacks are the same length, we can pop off last values until the two nodes are the same
        



*/

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (!root) return null;
    let pStack: TreeNode[] = [], qStack: TreeNode[] = [];

    function _generateStacks(root: TreeNode, stack: TreeNode[] = []): void {
        if (!root || (pStack.length && qStack.length)) return;

        stack.push(root);
        if (root === p) pStack = stack;
        if (root === q) qStack = stack;

        if (root.left) _generateStacks(root.left, [...stack]);
        if (root.right) _generateStacks(root.right, [...stack]);
    }

    _generateStacks(root);

    while (pStack.length !== qStack.length) {
        pStack.length > qStack.length ? pStack.pop() : qStack.pop();
    }

    while (pStack.length && qStack.length) {
        const pNode = pStack.pop()!;
        const qNode = qStack.pop()!;
        if (pNode === qNode) return pNode;
    }

    return null;
}

/*

According to ChatGPT:
    time complexity: O(n)
    space complexity: O(n)

*/