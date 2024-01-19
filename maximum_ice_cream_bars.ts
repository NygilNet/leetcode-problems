/*

link to leetcode: https://leetcode.com/problems/maximum-ice-cream-bars/description/

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Note: The boy can buy the ice cream bars in any order.

Return the maximum number of ice cream bars the boy can buy with coins coins.

You must solve the problem by counting sort.

*/

class Heap {
    heap = [];

    constructor() {
        this.heap = [];
    }




}

function maxIceCream(costs: number[], coins: number): number {

    // greedy approach: take lowest cost bars to maximize the number of bars

    const sorted = costs.slice(0).sort((a, b) => a - b);
    let totalBars = 0, totalCost = 0;

    for (const bar of sorted) {
        if (totalCost + bar > coins) break;
        totalCost += bar;
        totalBars++;

    }

    return totalBars;



    // heap solution

        // building a heap would be O(n)

        // using the heap would be O(logn)


}