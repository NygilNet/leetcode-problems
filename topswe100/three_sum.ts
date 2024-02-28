/*

link to problem: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

*/

function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const solution: number[][] = [], n = nums.length;
    let first = 0;

    while (first < n - 2) {
        const pointer = nums[first];
        let left = first + 1, right = n - 1;

        while (left < right) {
            const sum = pointer + nums[left] + nums[right];
            if (sum === 0) {
                solution.push([pointer, nums[left], nums[right]]);

                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;

                left++;
                right--;
                continue;
            }
            sum < 0 ? left++ : right --;
        }
        
        while (first < n - 2 && nums[first] === nums[first + 1]) first++;

        first++;
    }

    return solution;
}