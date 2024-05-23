"""

link to leetcode: https://leetcode.com/problems/the-number-of-beautiful-subsets/description/

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

"""

from collections import defaultdict
def beautifulSubsets(self, nums: list[int], k: int) -> int:
    # duplicated values are possible
    # backtracking approach
        # generate subsets
        # keep track of elements in subset in a dictionary
            # allows us to keep track of freq of values in subset (including duplicates)
        # if the subset would be invalid , stop traversing
    if len(nums) == 1:
        return 1
    
    freq = defaultdict(int)
    self.count = 0

    def _backtrack(i, subset):
        if i == len(nums):
            self.count += 1
            return 
        
        # if we skip current value
        _backtrack(i + 1, subset)

        # if we add current value and it's not bad
        if not subset[nums[i] - k] and not subset[nums[i] + k]:
            # add to subset
            subset[nums[i]] += 1
            # recurse with new index
            _backtrack(i + 1, subset)
            # remove from subset
            subset[nums[i]] -= 1


    _backtrack(0, freq)
    return self.count