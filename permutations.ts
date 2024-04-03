/*

link to leetcode: https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


Input: array of numbers
Output: array of arrays (all the possible combinations of characters)


all the possible -> backtracking


METHOD 1: BACKTRACKING

i. initialize return array as an empty array
ii. define a recursive function
    iii. take a number, and an array of remaining numbers
    iv. if array of remaining numbers in empty
        v. push stored array into result array

    vi. add new number to the array
    vii. call the function with the remaining characters


*/

function permute(nums: number[]): number[][] {
    const result: number[][] = [];

    function _backtracking(remaining: number[], res: number[]): void {
        if (!remaining.length) {
            result.push(res);
            return;
        }
        for (let i = 0; i < remaining.length; i++) {
            let nextNum = remaining[i];
            let nextRemaining = remaining.slice(0, i).concat(remaining.slice(i +1));
            _backtracking(nextRemaining, res.concat(nextNum));
        }
    }

    _backtracking(nums, []);
    return result;
};