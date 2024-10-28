"""
This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.


Input: string of repeated characters
Output: string where no two characters repeat or null


make a dictionary to keep a count of every character in the string

if the count of any characters is greater than half the length of the string, it will not be possible to make a string where no characters repeat


"""

from collections import defaultdict
class Solution:
    def rearrangeStringSoNoRepeats(self, s: str) -> str | None:
        N = len(s)
        chars_count = defaultdict(int)

        for char in s:
            chars_count[char] += 1
            if chars_count[char] > N // 2:
                return None
            
        rearranged = ""

        while chars_count:
            for key in chars_count:
                rearranged += key
                chars_count[key] -= 1
                if not chars_count[key]:
                    del chars_count[key]

        return rearranged