/*

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

*/

class lockableTreeNode {
    val: number
    left: lockableTreeNode | null
    right: lockableTreeNode | null
    private locked: boolean;

    constructor(val?: number, left?: lockableTreeNode | null, right?: lockableTreeNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
        this.locked = true;
    }

    is_locked(): boolean {
        return this.locked;
    }

    private _checkIfChildrenLocked(node: lockableTreeNode | null): boolean {
        if (!node || ((!node.left && !node.right) && node.is_locked())) {
            return true;
        }
        if ((node.left && !node.left.is_locked()) || (node.right && !node.right.is_locked())) {
            return false;
        }
        return this._checkIfChildrenLocked(node.left) && this._checkIfChildrenLocked(node.right);
    }

    private _checkIfChildrenUnlocked(node: lockableTreeNode | null): boolean {
        if (!node || ((!node.left && !node.right) && !node.is_locked())) {
            return true;
        }
        if ((node.left && node.left.is_locked()) || (node.right && node.right.is_locked())) {
            return false;
        }
        return this._checkIfChildrenUnlocked(node.left) && this._checkIfChildrenUnlocked(node.right);
    }

    lock(): boolean {
        if (this.is_locked()) {
            return false;
        }
        if (this._checkIfChildrenLocked(this.left) && this._checkIfChildrenLocked(this.right)) {
            this.locked = true;
            return true;
        }
        return false;
    }

    unlock(): boolean {
        if (!this.is_locked()) {
            return false;
        }
        if (this._checkIfChildrenUnlocked(this.left) && this._checkIfChildrenUnlocked(this.right)) {
            this.locked = false;
            return true;
        }
        return false;
    }
}
