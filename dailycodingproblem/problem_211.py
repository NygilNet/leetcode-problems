"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

class Solution:
    def allOccurrencesOfPattern(self, s: str, pattern: str) -> list[int]:
        N, PATTERN_LEN, FIRST_CHAR = len(s), len(pattern), pattern[0]
        res = []

        for i in range(N):
            if i + PATTERN_LEN > N:
                break

            char = s[i]
            if char == FIRST_CHAR and s[i : i + PATTERN_LEN] == pattern:
                res.append(i)

        return res
    
solution = Solution()
print(solution.allOccurrencesOfPattern("abracadabra", "abr")) # -> [0, 7]