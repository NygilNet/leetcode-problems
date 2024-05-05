"""
link to leetcode: https://leetcode.com/problems/sort-the-matrix-diagonally/description/

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Input: matrix
Output: matrix with every diagonal sorted




"""

def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(mat), len(mat[0])

    def _inbounds(r: int, c: int) -> bool:
        return (0 <= r < ROWS) and (0 <= c < COLS)

    def _findDiagonal(r: int, c: int):
        diagonal = ([(r, c)], [mat[r][c]])
        new_row, new_col = r + 1, c + 1

        while _inbounds(new_row, new_col):
            diagonal[0].append((new_row, new_col))
            diagonal[1].append((mat[new_row][new_col]))
            new_row += 1
            new_col += 1

        return diagonal

    def _sortDiagonal(coor, val):
        sort = sorted(val)

        for i in range(len(coor)):
            row, col = coor[i]
            mat[row][col] = sort[i]

    row = ROWS - 1
    col = 0

    while row >= 0:
        coor, val = _findDiagonal(row, col)
        _sortDiagonal(coor, val)
        row -= 1
    row = 0
    while col < COLS:
        coor, val = _findDiagonal(row, col)
        _sortDiagonal(coor, val)
        col += 1

    return mat