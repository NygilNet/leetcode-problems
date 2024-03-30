/*

link to leetcode: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/


You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

*/

function maxSubarrayLength(nums: number[], k: number): number {
    let longestSub: number = 0, left: number = 0;
    const frequencies: Map<number,number> = new Map();

    for (let right = 0; right < nums.length; right++) {
        const num = nums[right];
        frequencies.set(num, frequencies.get(num) + 1 || 1);

        while (frequencies.get(num)! > k) {
            const leftNum = nums[left];
            frequencies.set(leftNum, frequencies.get(leftNum)! - 1);
            left++;
        }

        longestSub = Math.max(longestSub, (right - left) + 1);
    }

    return longestSub;
}