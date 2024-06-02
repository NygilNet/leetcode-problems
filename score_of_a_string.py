"""
link to leetcode: https://leetcode.com/problems/score-of-a-string/submissions/1274814720/?envType=daily-question&envId=2024-06-01

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return ord(s)
        score = 0
        l, r = 0, 1

        while r < len(s):
            score += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1

        return score