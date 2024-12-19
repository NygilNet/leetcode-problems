"""
This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.


Input: array of integers
Output: boolean (does array contain a Pythagorean triplet)


"""

import math
class Solution:
    def containsPythogoreanTriplet(self, array: list[int]) -> bool:
        N = len(array)
        if N < 3:
            return False
        
        squared_array = [num * num for num in array]
        squared_array.sort()
       
        for i in range(N - 1, 1, -1):
            c_squared = squared_array[i]
            left, right = 0, i - 1
            while left < right:
                a_squared, b_squared = squared_array[left], squared_array[right]
                if a_squared + b_squared == c_squared:
                    return True
                elif a_squared + b_squared < c_squared:
                    left += 1
                else:
                    right -= 1

        return False
                    