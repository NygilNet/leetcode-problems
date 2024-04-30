"""

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.


input: array of integers
output: integer (maximum sum of biggest subarray)

has to be in O(N) time, so we iterate through the array once

return will not be negative


i. initialize max_sum @ 0 and current_sum @ 0
ii. iterate through the array
    iii. add array at i to current_sum
    iv. if current_sum is not negative
        v. set max_sum to max between current_sum and max_sum
    vi. else
        vii. reset current_sum to 0

"""

def maxSumOfContiguousSubarray(nums: list(int)) -> int:
    max_sum = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum >= 0:
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = 0

    return max_sum