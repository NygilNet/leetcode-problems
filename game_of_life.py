"""

link to problem: https://leetcode.com/problems/game-of-life/description/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

input: matrix (cells are either 0 or 1)
output: no output, modifying in place




"""

def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    ROWS, COLS = len(board), len(board[0])
    NEIGHBORS = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))
    COPY = deepcopy(board)

    def _inbounds(r: int, c: int) -> bool:
        return (0 <= r < ROWS) and (0 <= c < COLS)
    
    def _count_neighbors(r: int, c: int) -> int:
        sum = 0
        for dr, dc in NEIGHBORS:
            new_row, new_col = r + dr, c + dc
            sum += COPY[new_row][new_col] if _inbounds(new_row, new_col) else 0
        return sum

    for row in range(ROWS):
        for col in range(COLS):
            neighbors = _count_neighbors(row, col)
            if COPY[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    board[row][col] = 0
            else:
                if neighbors == 3:
                    board[row][col] = 1


                   