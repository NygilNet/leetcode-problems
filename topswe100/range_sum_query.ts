/*

link to problem: https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

*/

class NumArray {

    private prefixSum: number[];

    constructor(nums: number[]) {
        this.prefixSum = [0];
        let sum = 0;
        for (const num of nums) {
            sum += num;
            this.prefixSum.push(sum);
        }
    }

    sumRange(left: number, right: number): number {
        if (right > this.prefixSum.length || left < 0) throw new Error("Inputs are outside the range of the array.");
    
        return this.prefixSum[right + 1] - this.prefixSum[left];
    }

}

/*

original solution

    class NumArray {
        array: number[];

        constructor(nums: number[]) {
            this.array = nums;
        }

        sumRange(left: number, right: number): number {
            if (right > this.array.length || left < 0) throw new Error("Inputs are outside the range of the array.");
            let sum = 0;
            for (let i = left; i <= right; i++) {
                sum += this.array[i];
            }
            return sum;
        }

    }

While it did occur to me to use dynamic programming, I didn't originally see a way where it would make the design more efficient 

*/
