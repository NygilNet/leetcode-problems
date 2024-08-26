"""
This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

class Solution:
    def allPairsOfPalindromes(self, words: list[str]) -> list[tuple[int, int]]:
        def _isPalindrome(word: str) -> bool:
            # left, right = 0, len(word) - 1

            # while left < right:
            #     if word[left] != word[right]:
            #         return False
            #     left += 1
            #     right -= 1

            # return True
            return word == word[::-1]
        
        res = []
        for first in range(len(words)):
            for second in range(len(words)):
                if first == second:
                    continue

                if _isPalindrome(words[first] + words[second]):
                    res.append((first, second))

        return res
    

solution = Solution()
print(solution.allPairsOfPalindromes(["code", "edoc", "da", "d"])) # -> [(0, 1), (1, 0), (2, 3)]