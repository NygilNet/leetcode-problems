"""
link to leetcode: https://leetcode.com/problems/combination-sum-ii/description/?envType=daily-question&envId=2024-08-13

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Input: list of integers, target int
Output: list of lists


main issue might be making sure set doesn't contain duplicate combinations since different list have different references in memory


SOLUTION 1: Backtracking


"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # def _isSameArray(lst1: list, lst2: list) -> bool:
        #     if len(lst1) != len(lst2):
        #         return False
            
        #     set1 = set(lst1)
        #     set2 = set(lst2)
        #     return set1 == set2
        
        def _backtracking(i: int, lst: list[int] = []):
            if i >= len(candidates):
                return
            lst.append(candidates[i])
            if sum(lst) == target:
                if tuple(lst) not in seen:
                    seen.add(tuple(lst))
                    combinations.append(lst.copy())
                return
            _backtracking(i + 1, lst)
            lst.pop()
            _backtracking(i + 1)
            
                
        global seen
        seen = set()
        global combinations
        combinations = []

        candidates.sort()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            _backtracking(i)
        return combinations