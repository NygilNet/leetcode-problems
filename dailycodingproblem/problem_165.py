"""
This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

from collections import deque, defaultdict
class Solution:
    def howManySmallerElementsToRight(self, arr: list[int]) -> list[int]:
        res = deque()
        elements = defaultdict(int)

        for i in range(len(arr) - 1, -1, -1):
            current_num = arr[i]
            smaller_elements = 0

            for element in elements:
                if element < current_num:
                    smaller_elements += elements[element]
            
            res.appendleft(smaller_elements)
            elements[current_num] += 1

        return list(res)
    
solution = Solution()

print(solution.howManySmallerElementsToRight([3, 4, 9, 6, 1])) # -> [1, 1, 2, 1, 0]