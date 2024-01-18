/*

link to leetcode: https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

looks like a backtracking problem to me

initialize possible ways at 0

define a backtracking function

    - if number is equal to target increment possible ways and return

    - if number is greater than target, return

    - else recursively call function for current number plus and current number plus two

call backtracking function will 1 and 2

return possible ways

method passes test cases, but time limit is exceeded at 44


try to reverse the operation

    so instead of adding up to target, we start at the target and subtract to zero

still too slow




*/

function climbStairs(n: number): number {


    function countWays(num: number, arr: number[]) {
        if (num <= 1) return arr[num] = 1;
        if (arr[num] !== -1) return arr[num];

        arr[num] = countWays(num - 1, arr) + countWays(num - 2, arr);
        return arr[num];
    }

   let memo: number[] = [0].fill(-1, 0, n + 1);

   return countWays(n, memo);

}

/*

According to ChatGPT:
    original function time complexity: O(2^n)
    original function space complexity: O(n)

Searching for the the time and space complexity of the original function lead me towards memoization and dynamic programming. I believe this the first time I've encountered memoization 

Time complexity of memoized version is O(n)
Space complexity of memoized version is O(n) 

*/