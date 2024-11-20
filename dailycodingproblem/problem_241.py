"""
This problem was asked by Palantir.

In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.


Input: list of citation used in each paper
Output: number 


sort the list from greatest to least
iterate through sorted list
if i + 1 (adjusted for 0-index) is equal to number of citations used, return

"""


class Solution:
    def calculateHIndex(self, citations: list[int]) -> int:
        N = len(citations)
        from_greatest_to_least = sorted(citations, reverse=True)

        for i in range (N):
            citations_used = from_greatest_to_least[i]

            if i + 1 == citations_used:
                return citations_used
            
        return -1