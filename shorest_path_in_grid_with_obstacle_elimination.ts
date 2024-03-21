/*

link to leetcode: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

shortest path -> bfs

with our usual bfs template, we have to make a check if neighbor = 1 (call a new version of the function, decrease k and continue to check from neighbor) or if neighbor = 0 (continue as normal)


*/

function shortestPath(grid: number[][], k: number): number {
    const ROWS = grid.length, COLS = grid[0].length;
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    if (k >= ROWS + COLS - 3) {
        return ROWS + COLS - 2;
    }

    function _inbounds(r: number, c: number): boolean {
        return (0 <= r && r < ROWS) && (0 <= c && c < COLS);
    }

    const queue: number[][] = [[0, 0, 0, k]];
    const visited: Set<string> = new Set([`0,0,${k}`]);

    while (queue.length) {
        const [row, col, steps, remainingEliminations] = queue.shift()!;
        if (row === ROWS - 1 && col === COLS - 1) {
            return steps;
        }
        
        for (const [dr, dc] of DIRECTIONS) {
            let newRow = row + dr, newCol = col + dc;
            if (_inbounds(newRow, newCol)) {
                const newElims = remainingEliminations - grid[newRow][newCol];
                const key = `${newRow},${newCol},${newElims}`;
                if (newElims >= 0 && !visited.has(key)) {
                    queue.push([newRow, newCol, steps + 1, newElims]);
                    visited.add(key);
                }
            }
        }
    }
    
    return -1;
}