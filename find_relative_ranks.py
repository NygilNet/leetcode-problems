"""
link to problem: https://leetcode.com/problems/relative-ranks/
"""

def findRelativeRanks(self, score: List[int]) -> List[str]:
    arr = score.copy()
    arr.sort(reverse=True)
    d = {}
    for i,s in enumerate(arr):
        if i == 0: d[s] = "Gold Medal"
        elif i == 1: d[s] = "Silver Medal"
        elif i == 2: d[s] = "Bronze Medal"
        else: d[s] = str(i+1)
    for i,s in enumerate(score):
        score[i] = d[s]
    return score 