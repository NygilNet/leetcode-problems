"""
This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].


"""

from collections import defaultdict
class Solution:
    def largestSubsetSharesLCD(self, nums: list[int]) -> list[int]:
        lcds = defaultdict(list)
        contains_one = False
        sort = sorted(nums)

        for num in sort:
            if num == 1:
                contains_one = True
                continue

            found_lcd = False
            for key in lcds:
                if num % key == 0 or key % num == 0:
                    found_lcd = True
                    lcds[key].append(num)
                    break
            if not found_lcd:
                lcds[num].append(num)

        res = []

        for key in lcds:
            if len(res) < len(lcds[key]):
                res = lcds[key]

        if contains_one:
            res = [1] + res
        return res



set_1 = [3, 5, 10, 20, 21]
set_2 = [1, 3, 6, 24]

solution = Solution()
print(solution.largestSubsetSharesLCD(set_1)) # -> [5, 10, 20]
print(solution.largestSubsetSharesLCD(set_2)) # -> [1, 3, 6, 24]