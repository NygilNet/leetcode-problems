"""
This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""

class Solution:
    def findDuplicate(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            element = arr[mid]

            if arr[mid - 1] == element or arr[mid + 1] == element:
                return element
            elif element == mid:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    

solution = Solution()

print(solution.findDuplicate([1, 1, 2, 3, 4, 5, 6])) # -> 1
print(solution.findDuplicate([1, 2, 3, 4, 5, 6, 6])) # -> 6
print(solution.findDuplicate([1, 2, 2, 3, 4, 5, 6])) # -> 2