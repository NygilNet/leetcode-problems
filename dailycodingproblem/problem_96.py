"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

Input: list of integers
Output: list of lists


all possible permutations -> backtracking

"""

class Solution:
    def allPossiblePermutations(arr: list[int]) -> list[list[int]]:
        res = []

        def _backtracking(remaining: list[int], r: list[int] = []):
            if len(remaining) == 0:
                res.append(r)
                return
            for i in range(len(remaining)):  
                _backtracking(remaining[0 : i] + remaining[i + 1 :], r + [remaining[i]])
            
        _backtracking(arr)
        return res
    
print(Solution.allPossiblePermutations([1, 2, 3]))