"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

from collections import defaultdict
class Solution:
    def canRearrangeIntoPalindrome(s: str) -> bool:
        chars = defaultdict(int)

        for char in s:
            chars[char] += 1

        found_odd = False

        for key in chars:
            if chars[key] % 2 == 1:
                if found_odd:
                    return False
                found_odd = True

        return True
