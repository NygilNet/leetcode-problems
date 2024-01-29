/*

link to problem:  https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18

*/

function climbStairs(n: number): number {

    const len = n + 1, memo = new Array(len);

    for (let i = 0; i < len; i++) {
        const result = i <= 1 ? 1 : memo[i - 1] + memo[i - 2];
        memo[i] = result;
    }

    return memo[n];

}

/*

function climbStairs(n: number): number {


    function countWays(num: number, arr: number[]) {
        if (num <= 1) return arr[num] = 1;
        if (arr[num] !== -1) return arr[num];

        arr[num] = countWays(num - 1, arr) + countWays(num - 2, arr);
        return arr[num];
    }

   let memo: number[] = Array(n + 1).fill(-1);

   return countWays(n, memo);

}

*/