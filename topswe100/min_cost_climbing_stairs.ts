/*

link to problem: https://leetcode.com/problems/min-cost-climbing-stairs/description/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Input: number array
Output: number

looks like problem requires dynamic programming



10,         0               0
15,         10, 0           0
20,         10, 15          10
goal,       15, 30, 20      15

generate a memo of empty array, length = cost.length + 1
iterate through costs, index i
    if (i < 2) memo[i].push(0)
    if (i < 0) take 

    array is just getting bigger every index

generate a memo, length of cost + 1, filled with Infinity value
set indices 0 and 1 to 0
iterate through costs, index i
    result = cost[i] + memo[i]

    set the values of memo[i + 1] and memo[i + 2] to the minimum between their current value or result
return minimum cost at top floor

*/

function minCostClimbingStairs(cost: number[]): number {

    const len = cost.length, memo: number[] = new Array(len).fill(Infinity);
    
    memo[0] = 0;
    memo[1] = 0;

    for (let i = 0; i < len; i++) {
        let result = memo[i] + cost[i];
        memo[i + 1] = Math.min(result, memo[i + 1]);
        memo[i + 2] = Math.min(result, memo[i + 2]);
    }

    return memo[len - 1];

    /*
    
    const len = cost.length;
    let prev1 = 0, prev2 = 0;

    for (let i = 0; i < len; i++) {
        let result = cost[i] + Math.min(prev1, prev2);
        prev2 = prev1;
        prev1 = current;
    }

    return Math.min(prev1, prev2);
    
    */

}