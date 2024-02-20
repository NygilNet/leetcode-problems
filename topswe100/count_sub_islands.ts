/*

link to problem:

*/

function countSubIslands(grid1: number[][], grid2: number[][]): number {
    let maxArea = 0;
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]], numOfRows = grid1.length, numOfCols = grid1[0].length, visited = Array.from({ length: numOfCols }, () => new Array(numOfRows).fill(0));

    function _isInBounds(r: number, c: number): boolean {
        return (0 <= r && r < numOfRows) && (0 <= c && c < numOfCols); 
    }

    let subIslandCount = 0;
    function _countSubIsland() {
        
    }
    
    function _mapIsland(row: number, col: number) {
        const stack = [col, row];
        visited[row][col] = "X";
        while (stack.length) {
            const r = stack.pop()!;
            const c = stack.pop()!;
            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr, newCol = c + dc;
                if (_isInBounds(newRow, newCol) && grid1[newRow][newCol] === 1 && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = "X";
                    stack.push(newCol, newRow);
                } 
            }
        }
    }


    for (let row = 0; row < numOfRows; row++) {
        for (let col = 0; col < numOfCols; col++) {
            if (grid1[row][col] === 1 && !visited[row][col]) _mapIsland(row, col);    
        }
    }

    return subIslandCount;
}