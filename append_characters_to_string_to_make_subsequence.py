"""
link to leetcode: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03


You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.


Input: two strings
Output: number (minimum chars to add to end of s)


i. initialize i @ 0
ii. iterate over s and t while i is less than the length of t and s[i] and t[i] are the same character; increment i
iii. return length of t minus i


TWO-POINTER:
i. initialize a pointer for t @ 0
ii. iterate through s
    iii. if we encounter t[pointer] in the string, increment the pointer forward
iv. return the length of t[pointer:]

"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer = 0

        for char in s:
            if char is t[pointer]:
                pointer += 1
                if pointer == len(t):
                    return 0

        return len(t[pointer:])

        # length_of_t = len(t)
        # i = 0

        # while i < length_of_t and s[i] is t[i]:
        #     i += 1

        # return length_of_t - i