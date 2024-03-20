class TreeNode {
    constructor(val, left, right) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function problem8(root) {

    let count = 0;

    const stack = [root];

    while (stack.length) {
        const { val, left, right } = stack.pop();
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

const tree = new TreeNode(0, new TreeNode(1, null, null), new TreeNode(0, new TreeNode(1, new TreeNode(1, null, null), new TreeNode(1, null, null)), new TreeNode(0, null, null)));

console.log(problem8(tree));