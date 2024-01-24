/*

link to problem: https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

*/

function isPalindrome(s: string): boolean {

    const array = s.split("").filter(char => /[^_\W]+/g.test(char));
    
    for (let i = 0, j = array.length - 1; i < j; i++, j--) {
        if (array[i].toLowerCase() !== array[j].toLowerCase()) return false;
    }
    
    return true;

}