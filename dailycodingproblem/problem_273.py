"""
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.


Input: sorted array of ints
Output: positive int (index of fixed point) or boolean (false if no fixed point found)


I. Brute force
    - iterate through the array
    - if val @ index is equal to the index, return the index
    - if we finish iterating w/o returning, return false

II. Binary search
    - get N, length of array
    - set left to 0 and right to N - 1
    - while left is less than or equal to right
        - if values at left index and right index are both greater than N or less than 0, return false
        - calculate the midpoint between left and right
            - if val @ midpoint is equal to midpoint, return midpoint
            - if val @ midpoint is greater than midpoint, fixed point MUST be at left side of the array, so set right equal to midpoint - 1
            - else fixed point could be at right side of the array, set left equal to midpoint + 1
    - if function has not returned, return false

"""

class Solution:
    def findFixedPoint(self, array: list[int]):
        N = len(array)
        left, right = 0, N - 1

        while left <= right:
            if (array[left] < 0 and array[right] < 0) or (array[left] > N and array[right] > N):
                break
            midpoint = left + (right - left) // 2
            val = array[midpoint]

            if midpoint == val:
                return midpoint
            elif val > midpoint:
                right = midpoint - 1
            else:
                left = midpoint + 1
     
        return False
    

solution = Solution()

print(solution.findFixedPoint([-6, 0, 2, 40])) # -> 2
print(solution.findFixedPoint([1, 5, 7, 8])) # -> False