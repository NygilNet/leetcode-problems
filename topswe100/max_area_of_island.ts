/*

link to problem: https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

*/

function maxAreaOfIsland(grid: number[][]): number {
    let maxArea = 0;
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]], numOfRows = grid.length, numOfCols = grid[0].length, visited: Set<string> = new Set();

    function _isInBounds(r: number, c: number): boolean {
        return (0 <= r && r < numOfRows) && (0 <= c && c < numOfCols); 
    }

    function _mapIsland(row: number, col: number): number {
        let islandArea = 0;
        const stack = [col, row];
        visited.add(`${row},${col}`);
        while (stack.length) {
            islandArea++;
            const r = stack.pop()!;
            const c = stack.pop()!;
            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr, newCol = c + dc;
                if (_isInBounds(newRow, newCol) && grid[newRow][newCol] === 1 && !visited.has(`${newRow},${newCol}`)) {
                    visited.add(`${newRow},${newCol}`);
                    stack.push(newCol, newRow);
                } 
            }
        }
        return islandArea;
    }

    for (let row = 0; row < numOfRows; row++) {
        for (let col = 0; col < numOfCols; col++) {
            if (grid[row][col] === 1 && !visited.has(`${row},${col}`)) maxArea = Math.max(_mapIsland(row, col), maxArea);    
        }
    }

    return maxArea;
}