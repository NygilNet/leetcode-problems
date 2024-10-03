"""
This problem was asked by Twitter.

A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"]
"""

class Solution:
    def swapArrayBasedOnPermutation(self, arr: list, permutation: list[int]) -> None:
        memo = dict()

        for i in range(len(arr)):
            element = arr[i]
            p_i = permutation[i]

            if i == p_i:
                continue

            if p_i in memo:
                arr[i] = memo[p_i]
            else:
                arr[i] = arr[p_i]
                memo[i] = element


solution = Solution()
test = ['a', 'b', 'c']
solution.swapArrayBasedOnPermutation(test, [2, 1, 0])
print(test) # -> ['c', 'b', 'a']