"""
This problem was asked by Uber.

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.


Input: how many number in unlock pattern (int)
Output: number of valid unlock patterns (int)


limited number of inputs -> backtracking
create an adjacency list for each keypad number
run a backtracking function that tracks current pattern and visited keypads
when a valid pattern is created, save to a valid patterns list
when all valid patterns are created, return the length of valid patterns list

"""

class Solution:
    def numberOfValidUnlockPatterns(self, N: int) -> int:
        global keypadAdjacencyList
        keypadAdjacencyList = {
            1: (2, 4, 5),
            2: (1, 3, 4, 5, 6),
            3: (2, 5, 6),
            4: (1, 2, 5, 7, 8),
            5: (1, 2, 3, 4, 6, 7, 8, 9),
            6: (2, 3, 5, 8, 9),
            7: (4, 5, 8),
            8: (4, 5, 6, 7, 9),
            9: (5, 6, 8)
        }
        validPatterns = set()

        def _backtracking(currentKeypad: int, currentPattern: str, visited: set[int]):
            if len(currentPattern) == N:
                validPatterns.add(currentPattern)
                return
            
            for neighbor in keypadAdjacencyList[currentKeypad]:
                if neighbor not in visited:
                    copy = visited.copy()
                    copy.add(neighbor)
                    _backtracking(neighbor, currentPattern + str(neighbor), copy)

        for keypad in range (1, 10):
            _backtracking(keypad, str(keypad), set([keypad]))

        print(validPatterns)
        return len(validPatterns)

solution = Solution()
print(solution.numberOfValidUnlockPatterns(4))
