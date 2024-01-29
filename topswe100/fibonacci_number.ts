/*

link to problem: https://leetcode.com/problems/fibonacci-number/description/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

*/

function fib(n: number): number {

    const len = n + 1, memo = new Array(len);
    memo[0] = 0;

    for (let i = 1; i < len; i++) {
        const result = i <= 2 ? 1 : memo[i - 1] + memo[i - 2];
        memo[i] = result;
    }

    return memo[n];

}

/*

This is an example of using dynamic programming and memoization with a problem that would be too slow using a recursive solution

Demonstrates figuring out in what order you should solve a problem


*/