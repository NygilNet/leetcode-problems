"""

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

input: 2d matrix, target word
output: boolean (if the word can be found in the matrix)

bfs:
    i. iterate through the matrix until we find the first character of the target word
    ii. define a bfs helper function that will check the neighbors of the current character we are on (specifically left or down)
        iii. if we find all the characters of the word return true
        iv. else return false
    v. if the helper function returns true, return true
    vi. else continue to iterate through the matrix and find the first letter of the target again
    vii. if we iterate through the entire matrix w/o returning true, return false as the target word is not in the matrix

"""

def findTargetWordInMatrix(matrix: list[list[str]], target: str) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    NEIGHBORS = ((0, -1), (1, 0))

    def _inbounds(r: int, c: int) -> bool:
        return (0 <= r < ROWS) and (0 <= c < COLS)

    def _dfs(row: int, col: int, s: str, dr: int, dc: int) -> bool:
        if not s:
            return True
        new_row, new_col = row + dr, col + dc
        if _inbounds(new_row, new_col) and matrix[new_row][new_col] == s[0]:
            return _dfs(new_row, new_col, s[1:], dr, dc)
        else:
            return False
        
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == target[0]:
                for dr, dc in NEIGHBORS:
                    if _dfs(row + dr, col + dc, target[1:], dr, dc):
                        return True
    
    return False
