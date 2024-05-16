"""
link to problem: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

"""

def maxSubArray(nums: list[int]) -> int:
    max_sum, running_sum = max(nums), nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        running_sum += num
        max_sum = max(max_sum, running_sum)

        if num > running_sum:
            running_sum = num

    return max_sum