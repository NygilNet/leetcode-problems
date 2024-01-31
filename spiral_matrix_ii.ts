/*

link to problem: https://leetcode.com/problems/spiral-matrix-ii/description/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

*/

function generateMatrix(n: number): number[][] {

    let matrix: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    const numberOfCells = n ** 2, DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let row = 0, column = 0, dir = 0;

    for (let i = 1; i <= numberOfCells; i++) {
        matrix[row][column] = i;

        let [addToRow, addToColumn] = DIRECTIONS[dir];
        const nextRow = row + addToRow, nextColumn = column + addToColumn;

        if (0 > nextRow || nextRow >= n || 0 > nextColumn || nextColumn >= n || matrix[nextRow][nextColumn] !== 0) {
            dir = (dir + 1) % 4;
            [addToRow, addToColumn] = DIRECTIONS[dir];
        }

        row += addToRow;
        column += addToColumn;
    }

    return matrix;

}
