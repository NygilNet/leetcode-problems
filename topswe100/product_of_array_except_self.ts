/*

link to problem: https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Can do:
- key into array (O 1)
- set has (O 1)
- set look up (O 1)


Can not do:
- two pointer (o n log n)
- sort (O log n)

iterate through the array once to get total product of all the nums

iterate through the array again to divide nums[i] by the product

*/

function productExceptSelf(nums: number[]): number[] {
    const len = nums.length, res: number[] = Array.from({ length: len });

    let leftProduct: number = 1;
    for (let i = 0; i < len; i++) {
        res[i] = leftProduct;
        leftProduct *= nums[i];
    } 

    let rightProduct: number = 1;
    for (let i = len - 1; i >= 0; i--) {
        res[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return res;
}

/*
function productExceptSelf(nums: number[]): number[] {
    const len = nums.length, res: number[] = Array.from({ length: len });


    function _productOfOthers(index: number, runningProduct: number): number {
        if (index === len) return runningProduct;
        runningProduct *= nums[index];
        return _productOfOthers(index + 1, runningProduct);
    }

    let totalProduct: number = 1;

    for (let i = 0; i < len; i++) {
        res[i] = _productOfOthers(i + 1, totalProduct);
        totalProduct *= nums[i];
    } 

    return res;
}
*/