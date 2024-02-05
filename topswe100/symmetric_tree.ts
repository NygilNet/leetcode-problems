/*

link to problem: https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

breath-first search solution

set up two arrays for each side of the tree

traverse the tree layer by layer

make sure the left array is the reverse of the right array

    if it is not return false

if we travel of whole tree without returning false, return true

*/

function isSymmetric(root: TreeNode | null): boolean {

    if (!root.left && !root.right) return true;

    const leftSide = [[root.left]], rightSide = [[root.right]], emptyNode = new TreeNode();

    while (leftSide.length || rightSide.length) {

        const currentLeftLayer = leftSide.pop() || [], currentRightLayer = rightSide.pop() || [], len = currentLeftLayer.length;

        const nextLeftLayer = [], nextRightLayer = [];

        for (let i = 0; i < len; i++) {

            const leftNode = currentLeftLayer[i] || emptyNode, rightNode = currentRightLayer[i] || emptyNode;

            if (leftNode.val !== rightNode.val) return false;

            nextLeftLayer.push(leftNode.left, leftNode.right);
            nextRightLayer.push(rightNode.right, rightNode.left);

        }

        leftSide.push(nextLeftLayer);
        rightSide.push(nextRightLayer);

    }


    return true;

}

/*

function isSymmetric(root: TreeNode | null): boolean {
    if (!root) return true;

    function _isMirror = (left: TreeNode | null, right: TreeNode | null) {
        if (!left && !right) return true;
        if (!left || !right) return false;
        return (left.val === right.val) && _isMirror(left.left, right.right) && _isMirror(left.right, right.left);
    }

    return _isMirror(root.left, root.right);
}

*/