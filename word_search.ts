/*

link to leetcode: https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Since the matrix is NOT sorted, we will have to iterate through the matrix until we find the first character of the target word

if we find the target character we will iterate through the target word, checking neighbors for the next character in word that we have not already checked

if we find all the characters, we return true

if a character can not be found, we will reset our set and continue to iterate through the matrix

if we get to the end of the matrix without finding the string of characters or without finding the target character at all, return false

*/

function exist(board: string[][], word: string): boolean {
    const NEIGHBORINGDIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const rowLength = board.length, columnLength = board[0].length;
    let check = false;

    function _inBounds(row: number, col: number): boolean {
        return (0 <= row && row < rowLength) && (0 <= col && col < columnLength);
    }
    
    function _buildWord(row: number, col: number, i: number) {
        if (!_inBounds(row, col) || board[row][col] !== word[i]) return;
        if (i === word.length - 1) {
            check = true;
            return;
        }

        board[row][col] = "";
        for (const [r, c] of NEIGHBORINGDIRECTIONS) {
            _buildWord(row + r, col + c, i + 1);
        }
        board[row][col] = word[i];
        return;
    }

    for (let r = 0; r < rowLength; r++) {
        for (let c = 0; c < columnLength; c++) {
            _buildWord(r, c, 0);
            if (check) return check;
        }
    }

    return check;
};