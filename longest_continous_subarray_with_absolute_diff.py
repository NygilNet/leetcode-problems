"""
link to leetcode: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=daily-question&envId=2024-06-23

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.


Input: array of ints, and int (limit)
Output: int (size of subarray where absolute difference is less than or equal to limit)


two-pointer
- keep track of left and right, indices that are included in subarray
- keep track of maximum element in subarray
- smallest element that can be added to subarray is max - limit (no negative numbers in nums), so we can increment right if nums[i] is equal to or greater than max - limit, else increment left until nums[i] fulfills logic
- if nums[i] is greater than max, update max and make sure elements in subarray still greater than or equal to new max - limit
- keep track greatest difference between right and left
- return the largest difference between right and left
"""

from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        N = len(nums)
        increase = deque()
        decrease = deque()
        longest_subarray = 0
        left  = 0

        for right in range(N):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])

            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])

            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1

            longest_subarray = max(longest_subarray, right - left + 1)

        return longest_subarray

        # N = len(nums)
        # longest_subarray = 0
        # left, right = 0, 1
        # max_ele = nums[0]
        
        # def _calculateMinElement() -> int:
        #     return max_ele - limit

        # while right < N:
        #     current = nums[right]
        #     _min_ele = _calculateMinElement()

        #     if current > max_ele:
        #         max_ele = current
        #         _min_ele = _calculateMinElement()
        #     while max_ele > _min_ele + limit and left < right: 
        #         left += 1
        #         max_ele = max(max_ele, nums[left : right + 1])
            
        #     longest_subarray = max(longest_subarray, right - left)
        #     right += 1

        # return longest_subarray


solution = Solution()
print(solution.longestSubarray([8,2,4,7], 4)) # -> 2
print(solution.longestSubarray([10,1,2,4,7,2], 5)) # -> 4
print(solution.longestSubarray([4,2,2,2,4,4,2,2], 0)) # -> 3