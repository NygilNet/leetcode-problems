"""
link to leetcode: https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

input: array of ints
output: int (min number of INCREMENTS)


i. sort array in descending order
ii. iterate through the array

"""

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        a = sorted(nums, reverse=True)
        prev = a[0]
        ranges = []
        increments = 0

        for i in range(1, len(a)):
            num = a[i]
            upper_range, lower_range = ranges.pop() if len(ranges) else None
            if num < lower_range:
                if upper_range is not None:
                    ranges.push((upper_range, lower_range))
                upper_range = prev - 1
                lower_range = num + 1
            if prev == num:
                if not len(ranges):
                    increments += (a[0] - num)

            prev = num

        return increments