function problem23 (matrix, start, end) {
    const DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]], ROWS = matrix.length, COLS = matrix[0].length, queue = [[start[0], start[1], 0]];

    function _inbounds(r, c) {
        return (0 <= r && r < ROWS) && (0 <= c && c < COLS);
    }

    matrix[start[0]][start[1]] = true;

    while (queue.length) {
        const [ row, col, steps ] = queue.shift();
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

const matrix = [[false, false, false, false],
[true, true, false, true],
[false, false, false, false],
[false, false, false, false]];
const start = [3, 0];
const end = [0, 0]; 

console.log(problem23(matrix, start, end));