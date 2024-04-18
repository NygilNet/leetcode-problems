function problem38(N) {
    let arrangementCount = 0;
    const visited = Array.from({ length: N }, () => new Array(N).fill(false));
    const DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]];

    function _inbounds(r, c) {
        return (0 <= r && r < N) && (0 <= c && c < N);
    }

    function _placeQueen(row, col, b) {
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
    
    console.log(_placeQueen(Math.floor(N / 2), Math.floor(N / 2), visited));
    // function _populateBoard(startRow: number, startCol: number, board: boolean[][]): void {
    //     let count: number = 0;
    // }

    // for (let row = 0; row < N; row++) {
    //     for (let col = 0; col < N; col++) {
    //         _populateBoard(row, col, visited);
    //         visited[row][col] = true;
    //     }
    // }


    return arrangementCount;
}

console.log(problem38(7));