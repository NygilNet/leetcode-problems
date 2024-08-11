"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

"""

import random
class Solution:
    def generateBasedOnProbabilities(numbers: list[int], probabilities: list[float]) -> int:
        TARGET = random.uniform(0, 1)
        ranges = []
        for p in probabilities:
            ranges.append(ranges[-1] if ranges else 0 + p)
        if ranges[-1] != 1:
            raise Exception("probabilities do not add to 1")

        left, right = 0, len(ranges) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if ranges[mid] == TARGET:
                break
            elif ranges[mid] > TARGET:
                right = mid - 1
            else:
                left = mid + 1

        return numbers[left]

# import random
# class Solution:
#     def generateBasedOnProbabilities(numbers: list[int], probabilities: list[float]) -> int:
#         TARGET = random.uniform(0, 1)
#         prev = 0
#         running_total = 0

#         for i, p in enumerate(probabilities):
#             running_total += p

#             if prev <= TARGET <= running_total:
#                 return numbers[i]
            
#             prev = running_total