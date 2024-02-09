/*

link to problem: https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

iterative method

i. declare two stacks for each tree

ii. while there is items in each trees

    iii. pop out each node from the stack

    iv. if the two values do not equal each other return false

    v. push in left value or null if left node does not exist

    vi. push in right value or null if right node does not exist

vii. if we clear both stack without returning false, we can return true


*/

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    const stackP: (TreeNode | null)[] = [p], stackQ: (TreeNode | null)[] = [q];

    while (stackP.length || stackQ.length) {
        const pNode = stackP.pop();
        const qNode = stackQ.pop();

        if (!pNode && !qNode) continue;
        if (!pNode || !qNode || pNode.val !== qNode.val) return false;

        stackP.push(pNode!.left, pNode!.right);
        stackQ.push(qNode!.left, qNode!.right);
    }
    
    return true;   

    /*
    if (p === null && q === null) return true;
    if (p === null || q === null || p.val !== q.val) return false;

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    */
};

/*

According to ChatGPT:
    Time complexity : O(n) worst case
    Space complexity: O(n)

This is a problem I submitted a version of this function with a 81ms run compared to this version's 51ms

Need to work on;

    taking time to analyze if a recursive solution will cost more time or memory

*/