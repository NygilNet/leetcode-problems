"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

input: array of integers
output: int shows the most in the array

CAN NOT:
    iterate over the array while iterating (O(n^2))
    sort the array (O(n log n))
    map with different elements (O(number of unique elements in the array))

keeping track of the majority element

i. initialize a map with {arr[0]: 1}
ii. iterate over the array
    iii. if the element is the same of map[i]
        iv. increment map[i] and move on
        v. if map[i] is greater than (len(arr) / 2) return key

"""

def majorityElement(nums: list(int)) -> int:
    map = dict()

    for num in nums:
        if num not in map:
            map[num] = 0
        map[num] += 1
        if map[num] > len(nums) // 2:
            return num
        
    max_key = (0, 0)

    for key in map:
        if map[key] > max_key[0]:
            max_key = (map[key], key)

    return max_key[1]


"""

alt solution w/ constant space

suspect = nums[0]
count = 1

for i in range(1, len(nums)):
    num = nums[i]

    if num == suspect:
        count += 1
    else:
        count -= 1

    if count == 0:
        suspect = num
        count = 1

return suspect


"""
