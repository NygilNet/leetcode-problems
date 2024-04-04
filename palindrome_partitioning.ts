/*

link to leetcode: https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


all possible -> backtracking

METHOD 1: BACKTRACKING

for each call of the backtracking function (parameters: string, result: array of palindromes)
    if string is empty push result array in answer array
    iterate through the remaining letters
        if the substring (0, x) is a palindrome, concat to result and call backtracking on remaining letters

*/

function partition(s: string): string[][] {
    const res: string[][] = [];

    function _isPalindrome(s: string): boolean {
        for (let left = 0, right = s.length - 1;
            left < right;
            left++, right--) {
                if (s[left] !== s[right]) {
                    return false;
                }
            }
        return true;
    }

    function _backtracking(i: number, solution: string[]): void {
        if (i === s.length) {
            res.push(solution);
            return;
        }
        for (let j = i; j < s.length; j++) {
            const substring = s.slice(i, j + 1);
            if (_isPalindrome(substring)) {
                _backtracking(j + 1, solution.concat(substring));
            }
        }
    }

    _backtracking(0, []);
    return res;
}

/*
popping from solution array instead of creating  new array every time

function partition(s: string): string[][] {
    const res: string[][] = [];

    function _isPalindrome(s: string): boolean {
        for (let left = 0, right = s.length - 1;
            left < right;
            left++, right--) {
                if (s[left] !== s[right]) {
                    return false;
                }
            }
        return true;
    }

    function _backtracking(i: number, solution: string[]): void {
        if (i === s.length) {
            res.push([...solution]);
            return;
        }
        for (let j = i; j < s.length; j++) {
            const substring = s.slice(i, j + 1);
            if (_isPalindrome(substring)) {
                solution.push(substring)
                _backtracking(j + 1, solution);
                solution.pop();
            }
        }
    }

    _backtracking(0, []);
    return res;
}

*/