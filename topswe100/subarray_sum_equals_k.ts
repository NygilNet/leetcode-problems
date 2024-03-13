/*

link to problem: https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

Input: number array, target sum
Output: total number of subarrays that add to target sum

APPROACH 1: backtracking

Pros: data algo that iterates over all possible subarrays
Cons: might to be slow of a solution

i. initialize subarray count at 0
ii. define backtracking function
    iii. if index is greater than nums.length - 1, return
    iv. if currentSum + nums[index] is equal to target, increment subarray count and return



*/

function subarraySum(nums: number[], k: number): number {
    let count = 0, currentSum = 0;
    const len = nums.length, sumFrequencies = new Map<number, number>();

    sumFrequencies.set(0, 1);

    for (let i = 0; i < len; i++) {
        currentSum += nums[i];

        if (sumFrequencies.has(currentSum - k)) {
            count += sumFrequencies.get(currentSum - k)!;
        }

        const currentFrequency = sumFrequencies.get(currentSum) || 0;
        sumFrequencies.set(currentSum, currentFrequency + 1);
    }

    return count;
}
// let subarrayCount: number = 0;
// const len = nums.length, startedAt: boolean[] = new Array(len).fill(false);

// function _backtracking(startIndex: number, currentSum: number): void {
//     if (startIndex >= len) {
//         return;
//     }
//     currentSum += nums[startIndex];
//     if (currentSum === k) {
//         subarrayCount++;
//     }

//     _backtracking(startIndex + 1, currentSum);
//     if (!startedAt[startIndex + 1]) {
//         startedAt[startIndex + 1] = true;
//         _backtracking(startIndex + 1, 0);
//     }
// }

// startedAt[0] = true;
// _backtracking(0, 0);

// return subarrayCount;