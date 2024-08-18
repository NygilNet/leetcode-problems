"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

class Solution:
    def firstRecurringCharacter(string: str):
        seen = set()

        for char in string:
            if char in seen:
                return char
            seen.add(char)

        return None