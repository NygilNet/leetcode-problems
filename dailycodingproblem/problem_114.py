"""
This problem was asked by Facebook.

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

from collections import deque
class Solution:
    def reverseStringDelimiters(self, s: str, delimiters: set) -> str:
        # push words into deque and take words out as a stack
        words = deque()
        # push words into deque and take delimiters out as a queue
        delimiters_in_order = deque()

        word = ""

        for char in s:
            if char in delimiters:
                delimiters_in_order.append(char)
                words.append(word if word else '-1')
                word = ""
                continue
            word += char

        words.append(word)

        res = ""
        while words or delimiters_in_order:
            current_word = words.pop() if len(words) else ""
            current_delimiter = delimiters_in_order.popleft() if len(delimiters_in_order) else ""

            res += current_word if current_word != "-1" else ""
            res += current_delimiter

        return res
    
solution = Solution()
d = set(["/", ":"])
print(solution.reverseStringDelimiters("hello/world:here", d)) # -> "here/world:hello"
print(solution.reverseStringDelimiters("hello/world:here/", d))
print(solution.reverseStringDelimiters("hello//world:here", d))