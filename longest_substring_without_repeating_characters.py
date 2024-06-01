"""
link to leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest 
substring
 without repeating characters.

Input: string
Output: number


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        letters_encountered = {}
        start = 0
        length = 0
        N = len(s)

        for end in range(N):
            char = s[end]

            if char in letters_encountered and start <= letters_encountered[char]:
                length = max(length, end - start)
                start = letters_encountered[char] + 1

            letters_encountered[char] = end

        length = max(length, end - start + 1)
        return length


        # left = 0
        # longest = 1
        # N = len(s)

        # while left < N:
        #     right = left + 1
        #     letters_encountered = set()
        #     letters_encountered.add(s[left])

        #     while right < N and s[right] not in letters_encountered:
        #         letters_encountered.add(s[right])
        #         right += 1

        #     longest = max(longest, right - left)
        #     left += 1

        # return longest