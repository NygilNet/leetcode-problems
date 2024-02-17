/*

link to problem: https://leetcode.com/problems/number-of-islands/description/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

*/

function numIslands(grid: string[][]): number {
    let islandCount = 0;
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]], numOfRows = grid.length, numOfCols = grid[0].length, visited: Set<string> = new Set();

    function _isInBounds(r: number, c: number): boolean {
        return (0 <= r && r < numOfRows) && (0 <= c && c < numOfCols); 
    }

    function _mapIsland(row: number, col: number) {
        islandCount++;
        const stack = [col, row];
        visited.add(`${row},${col}`);
        while (stack.length) {
            const r = stack.pop()!;
            const c = stack.pop()!;
            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr, newCol = c + dc;
                if (_isInBounds(newRow, newCol) && grid[newRow][newCol] === "1" && !visited.has(`${newRow},${newCol}`)) {
                    visited.add(`${newRow},${newCol}`);
                    stack.push(newCol, newRow);
                } 
            }
        }
    }

    for (let row = 0; row < numOfRows; row++) {
        for (let col = 0; col < numOfCols; col++) {
            if (grid[row][col] === "1" && !visited.has(`${row},${col}`)) _mapIsland(row, col);    
        }
    }

    return islandCount;
}