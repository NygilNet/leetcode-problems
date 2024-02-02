/*

link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

greedy solution: two pointer

first pointer is the day we buy

set second pointer to the day after

while there are still days left

    calculate the profit we can make by selling the stock

    if our calculated profit is greater than our max profit, replace max profit


return max profit


what we are trying to do this find the combination of the smallest number to the biggest number that we can create

assume smallest = prices[0]

if prices[i] is smaller than smallest and there are still days left
    update smallest

else calculate profit and update max profit same as greedy solution

*/

function maxProfit(prices: number[]): number {
    const len = prices.length;
    if (len <= 1) return 0;

    let maxProfit = 0, smallest = prices[0];

    for (let i = 1; i < len; i++) {
        const currentPrice = prices[i];
        smallest = Math.min(smallest, currentPrice);
        maxProfit = Math.max(maxProfit, currentPrice - smallest);
    }

    return maxProfit;
};

// let maxProfit = 0, smallest = prices[0];
// const len = prices.length;

// for (let i = 1; i < len; i++) {

//     let currentPrice = prices[i];

//     if (currentPrice < smallest) {
//         smallest = currentPrice;
//         continue;
//     }

//     const profit = currentPrice - smallest;
//     maxProfit = Math.max(maxProfit, profit);

// }

// return maxProfit;


// let maxProfit = 0, left = 0;
// const len = prices.length;

// while (left < len) {
//     let buyPrice = prices[left], right = left + 1;
//     while (right < len) {
//         let sellPrice = prices[right];
//         const profit = sellPrice - buyPrice;
//         maxProfit = Math.max(maxProfit, profit);
//         right++;
//     }
//     left++;
// }

// return maxProfit;