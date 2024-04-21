"""

link to leetcode: https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


input: list of numbers
output: number (length of longest consecutive sequence)


CAN NOT:
    sort the array [ O (n log n) ]
    iterate through the array

assume is requires a map (since it's in the array and hashing section)

"""

def longestConsecutive(self, nums:List[int]) -> int:
    nums = set(nums)
    table = {}
    max_length = 0

    for num in nums:
        before = table.get(num - 1, 0)
        after = table.get(num + 1, 0)
        val = before + 1 + after
        table[num - before] = val
        table[num + after] = val
        max_length = max(max_length, val)

    return max_length