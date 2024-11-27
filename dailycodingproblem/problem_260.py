"""
This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].


Input: clue array
Output: one possible array consistent w/ the clue array


i. get N from length of clue array
ii. make res array of length N filled with -1
iii. iterate backwards through the res array and the clue array at the same time
iv. if value of the clue array == -, replace the current index of the res array with current number
v. once we reach the front of the res array, we can fill in the rest of the numbers where the value of the res array == -1
vi. return the res array
"""

class Solution:
    def reconstructArrayWithClue(self, clue: list[str]) -> list[int]:
        N = len(clue)
        res = [-1] * N
        current_val = 0

        for i in range(N - 1, -1, -1):
            current_clue = clue[i]

            if current_clue == "-":
                res[i] = current_val
                current_val += 1

        for i in range(N):
            if res[i] == -1:
                res[i] = current_val
                current_val += 1

        return res
    
solution = Solution()
print(solution.reconstructArrayWithClue([None, "+", "+", "-", "+"])) # -> [1, 2, 3, 0, 4]