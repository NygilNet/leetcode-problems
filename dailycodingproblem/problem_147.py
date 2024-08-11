"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""

class Solution:
    def reverse(self, lst: list, i: int, j: int):
        if j < i:
            raise Exception("value of j must be higher than i")
        if i > j:
            raise Exception("value of i must be less than j")
        left, right = i, j

        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1


    def sortUsingReverse(self, lst: list):

        for i in range(len(lst)):
            not_sorted = lst[i:]
            next_smallest = min(not_sorted)
            next_smallest_index = lst.index(next_smallest, i)

            if next_smallest_index != i:
                self.reverse(lst, i, next_smallest_index)