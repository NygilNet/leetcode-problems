/*

link to leetcode: https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

backtracking solution

initialize minSum at Infinity

define backtracking function

    if current node is undefined/null

        compare current sum to minSum and save whichever is smallest

        return

    add value of current node to current sum total

    recursive call backtracking on bottom three across nodes

iterate over the first row of matrix, calling backtracking on each node

return minSum


memoization/ dynamic programming

    dfs to check each different path

    select the lowest number that we can reach at each row

    need to DFS for each starting point on row 0

*/

function minFallingPathSum(matrix: number[][]): number {
    const n = matrix.length, memo = {};
    let minSum: number = Number.MAX_SAFE_INTEGER;

    function _inbound(c: number): boolean {
        return 0 <= c && c < n;
    }

    function _dp(r: number, c: number): number {
        if (!_inbound(c)) {
            return Number.MAX_SAFE_INTEGER;
        }
        if (r === n - 1) {
            return matrix[r][c];
        }
        const key = `${r},${c}`;
        if (key in memo) {
            return memo[key];
        }

        const left = _dp(r + 1, c - 1);
        const mid = _dp(r + 1, c);
        const right = _dp(r + 1, c + 1);

        memo[key] = Math.min(left, mid, right) + matrix[r][c];

        return memo[key];
    }

    for (let col = 0; col < n; col++) {
        minSum = Math.min(_dp(0, col), minSum);
    }

    return minSum;
};

// let minSum: number = Infinity;
// const length = matrix[0].length, directions = [[1, -1], [1, 0], [1, 1]];

// function _backtracking(row: number, col: number, currentSum: number) {

//     const node = matrix[row][col];
//     currentSum += node;


//     for (let dir of directions) {

//         const nextRow = row + dir[0], nextCol = col + dir[1];

//         if (nextRow === length) {
//             minSum = Math.min(minSum, currentSum);
//             return;
//         }
//         if (0 > nextCol || nextCol >= length) {
//             continue;
//         }

//         _backtracking(nextRow, nextCol, currentSum);

//     }

// }

// for (let i = 0; i < length; i++) {
//     _backtracking(0, i, 0);
// }

// return minSum;

/*

function minFallingPathSum(matrix: number[]): number {

    const colLength = matrix.length;
    const rowLength = matrix[0].length;

    if (colLength === 1 || rowLength === 1) return matrix[0][0];

    function findMinFallingPath(row, col, dp) {

        if (dp[row][col] !== Infinity) return dp[row][col];

        if (row === colLength - 1) {
            return dp[row][col] = matrix[row][col];
        }

    }

    const dp = new Array(colLength);
    let i = 0;

    while (i < row) {
        dp[i] = new Array(rowLength).fill(Infinity);
        i++;
    }

    let minSum = Infinity;

    for (let j = 0; j < rowLength; j++) {
        minSum = Math.min(minSum)
    }


}


*/