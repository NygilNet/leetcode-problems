"""
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.


Input: array of ints
Output: int ?


assuming the array is EXCLUSIVELY elements that all share a common denominator, the greatest common denominator will ALWAYS be the smallest element in the array

that seems really simple, so designing a solution where all the elements may not share a greatest common denominator

i. find the smallest element in the array
ii. iterate through the array
    iii. if current element % smallest element is NOT equal to 0
        iv. the array doesn't have a greatest common denominator, return null
v. return the smallest element

"""

class Solution:
    def greatestCommonDenominator(elements: list[int]) -> int | None:
        smallest = min(elements)
        if smallest == 1:
            return smallest

        for current in elements:
            if abs(current) % smallest != 0:
                return None
            
        return smallest