"""
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

input: string
output: string

i. convert string into list, values separated by space
ii. reverse the order of created list
iii. join list back into a string and return new string
"""

class Solution:
    def reverseWordsInString(self, s: str) -> str:
        list_of_words = s.split(" ")
        list_of_words.reverse()
        return " ".join(list_of_words)

solution = Solution()
print(solution.reverseWordsInString("hello world here")) # -> "here world hello"