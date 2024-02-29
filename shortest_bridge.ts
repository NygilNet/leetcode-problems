/*

link to leetcode: https://leetcode.com/problems/shortest-bridge/description/

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

keyword: shortest path -> BFS

1. find first island, find how far this island extends
2. BFS until we hit next island
3. return the level of bfs we reached

*/

function shortestBridge(grid: number[][]): number {
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]], n = grid.length;
    const visited: boolean[][] = Array.from({ length: n}, () => new Array(n).fill(false));
    const queue: number[][] = [];
    let found = false;

    function _isInBounds(r: number, c: number): boolean {
        return (0 <= r && r < n) && (0 <= c && c < n); 
    }

    function _dfs(row: number, col: number) {
        const stack = [col, row];
        while (stack.length) {
            const r = stack.pop()!;
            const c = stack.pop()!;
            visited[r][c] = true;
            queue.push([r, c]);
            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr, newCol = c + dc;
                if (_isInBounds(newRow, newCol) && grid[newRow][newCol] === 1 && !visited[newRow][newCol]) {
                    stack.push(newCol, newRow);
                } 
            }
        }
    }

    function _bfs(): number {
        let layer = 0;
        while (queue.length) {
            let snapshot = queue.length;
            for (let i = 0; i < snapshot; i++) {
                const [r, c] = queue.shift()!;
                for (const [dr, dc] of DIRECTIONS) {
                    const newRow = r + dr, newCol = c + dc;
                    if (_isInBounds(newRow, newCol) && !visited[newRow][newCol]) {
                        if (grid[newRow][newCol] === 1) return +layer;
                        visited[newRow][newCol] = true;
                        queue.push([newRow, newCol]);
                    }
                }
            }

            layer++;
        }
        return -1;
    }

    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            if (grid[row][col] === 1) {
                _dfs(row, col);
                found = true;
                break;
            }
        }
        if (found) break;
    }

    return _bfs();
}