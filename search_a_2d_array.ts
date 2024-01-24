/*

link to problem: https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

*/

function searchMatrix(matrix: number[][], target: number): boolean {

    let leftRow = 0, rightRow = matrix.length - 1, mid = Math.floor((leftRow + rightRow) / 2);
    let targetRow;

    while (leftRow <= rightRow) {
        let currentRow = matrix[mid];
        if (currentRow[0] <= target && target <= currentRow[currentRow.length - 1]) {
            targetRow = currentRow;
            break;
        }

        if (currentRow[0] > target) {
            rightRow = mid - 1;
        } else if (currentRow[currentRow.length - 1] < target) {
            leftRow = mid + 1;
        }

        mid = Math.floor((rightRow + leftRow) / 2);
    }

    targetRow ||= matrix[0];

    let left = 0, right = targetRow.length - 1, midpoint = Math.floor((left + right) / 2);

    while (left <= right) {
        let current = targetRow[midpoint];

        if (current === target) {
            return true;
        } else if (current < target) {
            left = midpoint + 1;
        } else {
            right = midpoint - 1;
        }

        midpoint = Math.floor((left + right) / 2);
    }

    return false;
   
};