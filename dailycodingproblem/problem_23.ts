/*

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.


Input: matrix (array of boolean arrays), tuple (start coordinates), tuple (end coordinates)
Output: number (min number of steps to reach end)


minimum number -> bfs

*/

function shortestPath(matrix: boolean[][], start: [number, number], end: [number, number]): number {
    const DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]], ROWS = matrix.length, COLS = matrix[0].length, queue: [number, number, number][] = [[start[0], start[1], 0]];

    function _inbounds(r: number, c: number): boolean {
        return (0 <= r && r < ROWS) && (0 <= c && c < COLS);
    }

    matrix[start[0]][start[1]] = true;

    while (queue.length) {
        const [ row, col, steps ] = queue.shift()!;
        if (row === end[0] && col === end[1]) {
            return steps;
        }
        for (const [dr, dc] of DIRECTIONS) {
            const newRow = row + dr, newCol = col + dc;
            if (_inbounds(newRow, newCol) && matrix[newRow][newCol] === false) {
                matrix[newRow][newCol] = true;
                queue.push([newRow, newCol, steps + 1]);
            }
        }
    }
    
    return -1;
}