/*

link to leetcode: https://leetcode.com/problems/island-perimeter/description/

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

*/

function islandPerimeter(grid: number[][]): number {
    let perimeter: number = 0;
    const ROWS = grid.length, COLS = grid[0].length;
    const DIRECTIONS: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    function _inbounds(r: number, c: number): boolean {
        return (0 <= r && r < ROWS) && (0 <= c && c < COLS);
    }

    function _bfs(r: number, c: number): void {
        const stack: [number, number][] = [[r, c]];

        while (stack.length) {
            const [r, c] = stack.pop()!;
            if (grid[r][c] === 2) {
                continue;
            }
            grid[r][c] = 2;

            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr;
                const newCol = c + dc;

                if (_inbounds(newRow, newCol) && grid[newRow][newCol] === 1) {
                    stack.push([newRow, newCol]);
                } else if (!_inbounds(newRow, newCol) || grid[newRow][newCol] === 0) {
                    perimeter++;
                }
            }
        }
    }

    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (grid[row][col] === 1) {
                _bfs(row, col);
                break;
            }
        }
    }

    return perimeter;
}