"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?


Input: array of ints, starting index
Output: int (index of nearest larger num)


i. start @ index i
ii. iterate left and right through the array at the same time
iii. if left > -1
iv. check if array[left] is greater than array[i]
v. if true, return left, if false continue
vi. repeat steps iv - v on the right side
vii. if we break out of loop left > -1 or right < len(array) w/o returning anything, return None 

"""

class Solution:
    def nearestLargerNumber(nums: list[int], i: int) -> int | None:
        left, right, N, largest = i - 1, i + 1, len(nums), max(nums)
        if nums[i] == largest:
            return None

        while left > -1 or right < N:
            if left > -1:
                if nums[left] > nums[i]:
                    return left
                left -= 1
            if right < N:
                if nums[right] > nums[i]:
                    return right
                right += 1
