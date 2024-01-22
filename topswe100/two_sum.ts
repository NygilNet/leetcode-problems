/*

link to problem: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

*/

function twoSum(nums: number[], target: number): number[] {

    const n = nums.length, map = new Map();

    for (let i = 0; i < n; i++) {

        let currentValue = nums[i];

        if (map.has(currentValue)) return [map.get(currentValue), i];

        map.set(target - currentValue, i);

    }

    return [-1];

}

/*

Done problem recently enough to remember solution

having a map we can access will allow us to return a solution in one pass of the array


*/