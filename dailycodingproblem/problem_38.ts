/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

*/

function numberOfQueens(N: number): number {
    let arrangementCount: number = 0;
    const visited: boolean[][] = Array.from({ length: N }, () => new Array(N).fill(false));
    const DIRECTIONS: number[][] = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]];

    function _inbounds(r: number, c: number): boolean {
        return (0 <= r && r < N) && (0 <= c && c < N);
    }

    function _placeQueen(row: number, col: number, b: boolean[][]): boolean[][] {
        b[row][col] = true;
        for (const [dr, dc] of DIRECTIONS) {
            let newRow = row + dr;
            let newCol = col + dc;
            while (_inbounds(newRow, newCol)) {
                b[newRow][newCol] = true;
                newRow += dr;
                newCol += dc;
            }
        }
        return b;
    }

    function _populateBoard(startRow: number, startCol: number, board: boolean[][]): void {
        let count: number = 0;
    }

    for (let row = 0; row < N; row++) {
        for (let col = 0; col < N; col++) {
            _populateBoard(row, col, visited);
            visited[row][col] = true;
        }
    }

    return arrangementCount;
}

console.log(numberOfQueens(3));