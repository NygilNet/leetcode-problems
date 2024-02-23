/*

link to problem: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.


since the string can only be one of two possible characters

i. set up a counter for "(" and ")" both at zero
ii. iterate over the string
iii. increment the appropriate counter
iv. return the maximum different between "(" - ")" and ")" - "("

two-pointer solution

i. set left = 0, right = s.length - 1, and counter to 0
ii. while left <= right
    iii. check if s[left] is "(" and s[right] is ")"
        iv. if true, increment left and decrement right
        v. if s[left] is "(" and s[right] is "("
            vi. increment counter to "add a correct closer" and decrement right
        vii. if s[left] is ")" or left = right
            viii. increment counter and increment left

*/

function minAddToMakeValid(s: string): number {
    let counter = 0;
    let unmatchedOpen = 0;

    for (const char of s) {
        if (char === "(") {
            unmatchedOpen++;
        } else if (char === ")" && unmatchedOpen > 0) {
            unmatchedOpen--;
        } else {
            counter++;
        }
    }

    counter += unmatchedOpen;
    return counter;
}

/*

function minAddToMakeValid(s: string): number {
    let left = 0, right = s.length - 1, counter = 0;

    while (left <= right) {
        if (s[left] === "(" && s[right] === ")") {
            left++;
            right--;
        } else if (s[left] === "(" && s[right] === "(") {
            counter++;
            right--;
        } else {
            counter++;
            left++;
        }
    }

    return counter;
};

function minAddToMakeValid(s: string): number {
    const counter = {
        "(": 0,
        ")": 0
    }

    for (const c of s) {
        counter[c]++;
    }

    return Math.max(counter["("] - counter[")"], counter[")"] - counter["("]);
};

*/