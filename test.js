function shortestBridge(grid) {
    const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]], n = grid.length;
    const visited = Array.from({ length: n}, () => new Array(n).fill(false));
    const queue = [];

    function _isInBounds(r, c){
        return (0 <= r && r < n) && (0 <= c && c < n); 
    }

    function _dfs(row, col) {
        console.log("depth first search function start")
        const stack = [col, row];
        while (stack.length) {
            console.log("visited", visited)
            const r = stack.pop();
            const c = stack.pop();
            visited[r][c] = true;
            queue.push(`${r},${c}`);
            for (const [dr, dc] of DIRECTIONS) {
                const newRow = r + dr, newCol = c + dc;
                if (_isInBounds(newRow, newCol) && grid[newRow][newCol] === 1 && !visited[newRow][newCol]) {
                    stack.push(newCol, newRow);
                } 
            }
        }
        console.log("depth first search function end")
    }

    function _bfs(){
        let layer = 0;
        while (queue.length) {
            let snapshot = queue.length;

            for (let i = 0; i < snapshot; i++) {
                const coor = queue.shift();
                const [r, c] = coor.split(",");
                for (const [dr, dc] of DIRECTIONS) {
                    const newRow = +r + dr, newCol = +c + dc;
                    const key = `${newRow},${newCol}`;
                    if (_isInBounds(newRow, newCol) && !visited[newRow][newCol]) {
                        if (grid[newRow][newCol] === 1) return +layer;
                        visited[newRow][newCol] = true;
                        queue.push(key);
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
                break;
            }
        }
    }

    return _bfs();
}

const grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]];
console.log(shortestBridge(grid)); // Output: Expected shortest bridge length