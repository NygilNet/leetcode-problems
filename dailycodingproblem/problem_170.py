"""
This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.
"""

from collections import deque
class Solution:
    def shortestTransformation(self, start: str, end: str, dictionary: dict[str]) -> list[str]:
        if end not in dictionary:
            return None

        stack = deque()
        stack.append((start, [start]))
        visited = set()
        visited.add(start)

        while stack:
            current_word, path = stack.pop()

            if current_word == end:
                return path

            for i in range(len(current_word)):
                if current_word[i] == end[i]:
                    continue
                transformation = current_word[:i] + end[i] + current_word[i + 1:]

                if transformation in dictionary and transformation not in visited:
                    visited.add(transformation)
                    stack.append((transformation, path.copy() + [transformation]))

        return None
    
solution = Solution()
print(solution.shortestTransformation("dog", "cat", {"dot", "dop", "dat", "cat"}))
print(solution.shortestTransformation("dog", "cat", {"dot", "tod", "dat", "dar"}))