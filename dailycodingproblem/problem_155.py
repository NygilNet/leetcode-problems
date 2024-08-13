"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

from collections import defaultdict
class Solution:
    def findMajorityElement(lst: list[int]) -> int:
        map = defaultdict(int)
        map[lst[0]] = 1
        majority_element = (1, lst[0])

        for i in range(1, len(lst)):
            element = lst[i]

            map[element] += 1

            if map[element] > len(lst) // 2:
                return element
            if map[element] >= majority_element[0]:
                majority_element = (map[element], element)

        return majority_element[1]