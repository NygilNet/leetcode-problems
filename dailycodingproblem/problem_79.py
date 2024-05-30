"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

"""

class Solution:
    def isArrayNonDecreasing(arr: list[int]) -> bool:
        if len(arr) <= 1:
            return True

        change_made = False
        prev = arr.pop()
        while arr:
            current = arr.pop()

            if current > prev:
                if not change_made:
                    change_made = True
                    continue
                else:
                    return False
                
            prev = current
        
        return True